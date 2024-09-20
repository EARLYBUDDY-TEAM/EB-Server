from fastapi.testclient import TestClient
from eb_fast_api.main import app


def test_verifyTokenInRouter_SUCCESS(realJWTService):
    # given
    email = "test@test.com"
    accessToken = realJWTService.createAccessToken(email=email)
    headers = {"access-token": accessToken}
    testClient = TestClient(app)

    # when
    response = testClient.get(
        "/test_token_service/test_token",
        headers=headers,
    )

    # then
    responseModel = response.json()
    responseEmail = responseModel["userEmail"]
    assert email == responseEmail


def test_verifyTokenInRouter_FAIL(realJWTService):
    # given
    email = "test@test.com"
    realJWTService.accessTokenExpireMinute = -10
    expiredToken = realJWTService.createAccessToken(email=email)
    headers = {"access-token": expiredToken}
    testClient = TestClient(app)

    # when
    response = testClient.get(
        "/test_token_service/test_token",
        headers=headers,
    )

    # then
    responseBody = response.json()
    assert responseBody["detail"] == "토큰 만료"
    assert response.status_code == 490
