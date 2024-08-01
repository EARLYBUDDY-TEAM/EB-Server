from fastapi.testclient import TestClient
from eb_fast_api.main import app

from eb_fast_api.database.tests import conftest

from eb_fast_api.database.sources.database import get_db


client = TestClient(app)


app.dependency_overrides[get_db] = conftest.mockSession


def test_login_for_access_token_ERROR_no_user():
    json = {"email": "abcd@naver.com", "password": "password12"}
    response = client.post("/auth/login", json=json)
    assert response.status_code == 400
