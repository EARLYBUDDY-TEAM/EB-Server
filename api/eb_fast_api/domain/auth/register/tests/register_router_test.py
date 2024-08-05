from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.schema.sources.schema import UserInfo


def test_register_FAIL_invalid_register_info(testClient):
    userInfo = UserInfo(email = "abc@abc", password = "password12")
    json = userInfo.model_dump(mode = "json")
    response = testClient.post("/auth/register", json=json)

    assert response.status_code == 400


def test_register_FAIL_exist_user(registerMockDB):
    # given
    email = "abc@abc.com"
    password = "password12"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
    registerMockDB.userCreate(user)

    def getMockDB():
        yield registerMockDB

    app.dependency_overrides[getDB] = getMockDB
    testClient = TestClient(app)

    # when
    json = userInfo.model_dump(mode = "json")
    response = testClient.post("/auth/register", json=json)

    # then
    assert response.status_code == 401
    del app.dependency_overrides[getDB]


def test_register_SUCCESS(testClient):
    email = "abc@abc.com"
    password = "password12"
    userInfo = UserInfo(email, password)
    json = userInfo.model_dump(mode = "json")
    response = testClient.post("/auth/register", json=json)

    # then
    assert response.status_code == 200