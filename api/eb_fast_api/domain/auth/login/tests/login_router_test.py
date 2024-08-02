def test_login_for_access_token_ERROR_no_user(testClient):
    json = {"email": "abcd@naver.com", "password": "password12"}
    response = testClient.post("/auth/login", json=json)
    assert response.status_code == 400