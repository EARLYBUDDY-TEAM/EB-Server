import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from eb_fast_api.service.jwt.sources.token_service import verifyToken
from eb_fast_api.main import app


def test_verifyToken_SUCCESS(realJWTService):
    # given
    email = "test@test.com"
    notExpiredToken = realJWTService.createAccessToken(email=email)

    # when
    expectEmail = verifyToken(notExpiredToken)

    # then
    assert email == expectEmail


def test_verifyToken_FAIL(realJWTService):
    # given
    email = "test@test.com"
    realJWTService.accessTokenExpireMinute = -10
    expiredToken = realJWTService.createAccessToken(email=email)

    # when
    with pytest.raises(HTTPException) as context:
        verifyToken(expiredToken)

    # then
    assert isinstance(context.value, HTTPException)
    assert context.value.status_code == 490
    assert context.value.detail == "토큰 만료"


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
