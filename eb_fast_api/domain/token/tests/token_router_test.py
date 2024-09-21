from eb_fast_api.domain.schema.sources.schema import Token, UserInfo
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from fastapi.testclient import TestClient
from eb_fast_api.main import app


def test_getUserEmailInRouter_SUCCESS(
    mockTestClient,
    realJWTService,
):
    # given
    email = "test@test.com"
    refreshToken = realJWTService.createAccessToken(email=email)
    headers = {"access_token": refreshToken}

    # when
    response = mockTestClient.get(
        "/token/test_get_user_email_in_router",
        headers=headers,
    )

    # then
    responseModel = response.json()
    responseEmail = responseModel["userEmail"]
    assert email == responseEmail


def test_getUserEmailInRouter_FAIL(
    mockTestClient,
    realJWTService,
):
    # given
    email = "test@test.com"
    realJWTService.accessTokenExpireMinute = -10
    expiredToken = realJWTService.createAccessToken(email=email)
    headers = {"access_token": expiredToken}

    # when
    response = mockTestClient.get(
        "/token/test_get_user_email_in_router",
        headers=headers,
    )

    # then
    responseBody = response.json()
    assert responseBody["detail"] == "토큰 만료"
    assert response.status_code == 490


def test_recreateToken_Success(
    realJWTService,
    tokenMockJWTService,
    tokenMockUserCRUD,
    tokenMockScheduleCRUD,
):
    # given
    email = "test@test.com"
    email = "email"
    password = "password12"
    refreshToken = "refreshToken"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser(refreshToken=refreshToken)
    tokenMockUserCRUD.create(user)
    refreshToken = realJWTService.createRefreshToken(email=email)
    headers = {"refresh_token": refreshToken}

    def getMockUserCRUD():
        yield tokenMockUserCRUD

    def getMockJWTService():
        yield tokenMockJWTService

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    app.dependency_overrides[getJWTService] = getMockJWTService
    testClient = TestClient(app)

    # when
    response = testClient.get(
        "/token/recreate",
        headers=headers,
    )

    # then
    assert response.status_code == 200

    expectAccessToken = tokenMockJWTService.createAccessToken(email=email)
    expectRefreshToken = tokenMockJWTService.createRefreshToken(email=email)
    expectToken = Token(
        accessToken=expectAccessToken,
        refreshToken=expectRefreshToken,
    ).model_dump(mode="json")
    responseToken = response.json()
    assert expectToken == responseToken

    expectUser = tokenMockUserCRUD.read(email=email)
    assert expectUser.refreshToken == expectRefreshToken

    # restore dependency
    del app.dependency_overrides[EBDataBase.user.getCRUD]
    del app.dependency_overrides[getJWTService]

    # delete schedule table
    tokenMockScheduleCRUD.dropTable(userEmail=user.email)


def test_recreateToken_FAIL(
    mockTestClient,
    realJWTService,
):
    # given
    email = "test@test.com"
    realJWTService.refreshTokenExpireDay = -10
    expiredToken = realJWTService.createRefreshToken(email=email)
    headers = {"refresh_token": expiredToken}

    # when
    response = mockTestClient.get(
        "/token/recreate",
        headers=headers,
    )

    # then
    responseBody = response.json()
    assert responseBody["detail"] == "토큰 만료"
    assert response.status_code == 490
