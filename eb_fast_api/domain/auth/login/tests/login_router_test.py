from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schemas import TokenInfo, LoginInfo
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.sources.model.user import User
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.snippets.sources import pwdcrypt


def test_login_ERROR_no_user(testClient):
    json = {"email": "email", "password": "password12"}
    response = testClient.post("/auth/login", json=json)

    assert response.status_code == 400


def test_login_ERROR_invalid_password(
    loginMockUserCRUD,
    loginMockScheduleCRUD,
    loginMockRouteCRUD,
):
    try:
        # given
        email = "email"
        password = "password12"
        refreshToken = "refreshToken"
        loginInfo = LoginInfo(email=email, password=password)
        hashedPassword = pwdcrypt.hash(password)
        user = User.mock(
            email=email,
            refreshToken=refreshToken,
            hashedPassword=hashedPassword,
        )
        loginMockUserCRUD.create(user)

        def getMockUserCRUD():
            yield loginMockUserCRUD

        app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
        testClient = TestClient(app)

        # when
        loginInfo.password += "errorString"
        json = loginInfo.model_dump(mode="json")
        response = testClient.post("/auth/login", json=json)

        # then
        assert response.status_code == 401
        del app.dependency_overrides[EBDataBase.user.getCRUD]

    finally:
        # delete schedule table
        loginMockScheduleCRUD.dropTable(userEmail=user.email)
        loginMockRouteCRUD.dropTable(user_email=user.email)


def test_login_SUCCESS(
    loginMockUserCRUD,
    loginMockScheduleCRUD,
    loginMockJWTService,
    loginMockRouteCRUD,
):
    try:
        # given
        email = "email"
        password = "password12"
        refreshToken = "refreshToken"
        loginInfo = LoginInfo(
            email=email,
            password=password,
        )
        hashedPassword = pwdcrypt.hash(password)
        user = User.mock(
            email=email,
            refreshToken=refreshToken,
            hashedPassword=hashedPassword,
        )
        loginMockUserCRUD.create(user)

        def getMockUserCRUD():
            yield loginMockUserCRUD

        def getMockJWTService():
            yield loginMockJWTService

        app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
        app.dependency_overrides[getJWTService] = getMockJWTService
        testClient = TestClient(app)

        # when
        json = loginInfo.model_dump(mode="json")
        response = testClient.post("/auth/login", json=json)

        # then
        assert response.status_code == 200

        expectAccessToken = loginMockJWTService.createAccessToken(email=email)
        expectRefreshToken = loginMockJWTService.createRefreshToken(email=email)
        expectToken = TokenInfo(
            accessToken=expectAccessToken,
            refreshToken=expectRefreshToken,
        ).model_dump(mode="json")
        responseToken = response.json()
        assert expectToken == responseToken

        expectUser = loginMockUserCRUD.read(email=email)
        assert expectUser["refreshToken"] == expectRefreshToken

        # restore dependency
        del app.dependency_overrides[EBDataBase.user.getCRUD]
        del app.dependency_overrides[getJWTService]

    finally:
        # delete schedule table
        loginMockScheduleCRUD.dropTable(userEmail=user.email)
        loginMockRouteCRUD.dropTable(user_email=user.email)
