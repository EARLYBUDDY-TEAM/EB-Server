from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.models import User
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.snippets.sources import pwdcrypt


def test_login_for_access_token_ERROR_no_user(testClient):
    json = {"email": "abcd@naver.com", "password": "password12"}
    response = testClient.post("/auth/login", json=json)

    assert response.status_code == 400


def test_login_for_access_token_ERROR_invalid_password(loginMockDB):
    # given
    email = "email"
    password = "password12"
    user = User(
        email=email,
        hashedPassword=pwdcrypt.hash(password),
    )
    loginMockDB.userCreate(user)

    def getMockDB():
        yield loginMockDB

    app.dependency_overrides[getDB] = getMockDB
    testClient = TestClient(app)

    # when
    json = {
        "email": email,
        "password": password + "errorString",
    }
    response = testClient.post("/auth/login", json=json)

    # then
    assert response.status_code == 401

    del app.dependency_overrides[getDB]


def test_login_for_access_token_SUCCESS(loginMockDB):
    # given
    email = "email"
    password = "password12"
    user = User(
        email=email,
        hashedPassword=pwdcrypt.hash(password),
    )
    loginMockDB.userCreate(user)

    def getMockDB():
        yield loginMockDB

    app.dependency_overrides[getDB] = getMockDB
    testClient = TestClient(app)

    # when
    json = {
        "email": email,
        "password": password,
    }
    response = testClient.post("/auth/login", json=json)

    # then
    assert response.status_code == 200

    del app.dependency_overrides[getDB]