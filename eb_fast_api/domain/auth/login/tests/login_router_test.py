from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schema import UserInfo, Token
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService


def test_login_ERROR_no_user(testClient):
    json = {"email": "email", "password": "password12"}
    response = testClient.post("/auth/login", json=json)

    assert response.status_code == 400


def test_login_ERROR_invalid_password(
    loginMockUserCRUD,
    loginMockScheduleCRUD,
):
    # given
    email = "email"
    password = "password12"
    refreshToken = "refreshToken"
    userInfo = UserInfo(email=email, password=password)
    user = userInfo.toUser(refreshToken=refreshToken)
    loginMockUserCRUD.create(user)

    def getMockUserCRUD():
        yield loginMockUserCRUD

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    testClient = TestClient(app)

    # when
    userInfo.password += "errorString"
    json = userInfo.model_dump(mode="json")
    response = testClient.post("/auth/login", json=json)

    # then
    assert response.status_code == 401
    del app.dependency_overrides[EBDataBase.user.getCRUD]

    # delete schedule table
    loginMockScheduleCRUD.dropTable(userEmail=user.email)


def test_login_SUCCESS(
    loginMockUserCRUD,
    loginMockScheduleCRUD,
    loginMockJWTService,
):
    # given
    email = "email"
    password = "password12"
    refreshToken = "refreshToken"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser(refreshToken=refreshToken)
    loginMockUserCRUD.create(user)

    def getMockUserCRUD():
        yield loginMockUserCRUD

    def getMockJWTService():
        yield loginMockJWTService

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    app.dependency_overrides[getJWTService] = getMockJWTService
    testClient = TestClient(app)

    # when
    json = userInfo.model_dump(mode="json")
    response = testClient.post("/auth/login", json=json)

    # then
    assert response.status_code == 200

    expectAccessToken = loginMockJWTService.createAccessToken(email=email)
    expectRefreshToken = loginMockJWTService.createRefreshToken(email=email)
    expectToken = Token(
        accessToken=expectAccessToken,
        refreshToken=expectRefreshToken,
    ).model_dump(mode="json")
    responseToken = response.json()
    assert expectToken == responseToken

    expectUser = loginMockUserCRUD.read(email=email)
    assert expectUser.refreshToken == expectRefreshToken

    # restore dependency
    del app.dependency_overrides[EBDataBase.user.getCRUD]
    del app.dependency_overrides[getJWTService]

    # delete schedule table
    loginMockScheduleCRUD.dropTable(userEmail=user.email)
