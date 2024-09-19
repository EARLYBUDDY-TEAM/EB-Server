from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schema import UserInfo, Token
from eb_fast_api.database.sources.database import EBDataBase


def test_register_FAIL_invalid_register_info(testClient):
    invalidEmail = "abc@abc"
    password = "password12"
    userInfo = UserInfo(email=invalidEmail, password=password)
    json = userInfo.model_dump(mode="json")
    response = testClient.post("/auth/register", json=json)

    assert response.status_code == 400


def test_register_FAIL_exist_user(
    registerMockUserCRUD,
    registerMockScheduleCRUD,
):
    # given
    email = "abc@abc.com"
    password = "password12"
    refreshToken = "refreshToken"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser(refreshToken=refreshToken)
    registerMockUserCRUD.create(user)

    def getMockRegisterCRUD():
        yield registerMockUserCRUD

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockRegisterCRUD
    testClient = TestClient(app)

    # when
    json = userInfo.model_dump(mode="json")
    response = testClient.post("/auth/register", json=json)

    # then
    assert response.status_code == 401
    del app.dependency_overrides[EBDataBase.user.getCRUD]

    # delete schedule table
    registerMockScheduleCRUD.dropAll(userEmail=email)


def test_register_SUCCESS(
    testClient,
    registerMockJWTService,
    registerMockScheduleCRUD,
):
    # given
    email = "abc@abc.com"
    password = "password12"
    userInfo = UserInfo(email, password)
    json = userInfo.model_dump(mode="json")

    # when
    response = testClient.post("/auth/register", json=json)

    # then
    assert response.status_code == 200

    expectAccessToken = registerMockJWTService.createAccessToken(email=email)
    expectRefreshToken = registerMockJWTService.createRefreshToken(email=email)
    expectToken = Token(
        accessToken=expectAccessToken,
        refreshToken=expectRefreshToken,
    ).model_dump(mode="json")
    resultToken = response.json()
    assert expectToken == resultToken

    # delete schedule table
    registerMockScheduleCRUD.dropAll(userEmail=email)
