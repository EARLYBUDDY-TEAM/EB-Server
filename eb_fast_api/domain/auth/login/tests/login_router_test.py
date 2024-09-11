from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schema import UserInfo
from eb_fast_api.database.sources.database import EBDataBase


def test_login_ERROR_no_user(testClient):
    json = {"email": "email", "password": "password12"}
    response = testClient.post("/auth/login", json=json)

    assert response.status_code == 400


def test_login_ERROR_invalid_password(loginMockUserCRUD):
    # given
    email = "email"
    password = "password12"
    userInfo = UserInfo(email=email, password=password)
    user = userInfo.toUser()
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


def test_login_SUCCESS(loginMockUserCRUD):
    # given
    email = "email"
    password = "password12"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
    loginMockUserCRUD.create(user)

    def getMockUserCRUD():
        yield loginMockUserCRUD

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    testClient = TestClient(app)

    # when
    json = userInfo.model_dump(mode="json")
    response = testClient.post("/auth/login", json=json)

    # then
    assert response.status_code == 200
    del app.dependency_overrides[EBDataBase.user.getCRUD]
