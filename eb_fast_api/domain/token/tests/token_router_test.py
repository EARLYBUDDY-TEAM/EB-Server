from eb_fast_api.domain.schema.sources.schema import Token, RegisterInfo
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from fastapi.testclient import TestClient
from eb_fast_api.main import app


def test_recreateToken_Success(
    realJWTService,
    tokenMockJWTService,
    tokenMockUserCRUD,
    tokenMockScheduleCRUD,
):
    try:
        # given
        email = "test@test.com"
        email = "email"
        password = "password12"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
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
        assert expectUser["refreshToken"] == expectRefreshToken

        # restore dependency
        del app.dependency_overrides[EBDataBase.user.getCRUD]
        del app.dependency_overrides[getJWTService]

    finally:
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
