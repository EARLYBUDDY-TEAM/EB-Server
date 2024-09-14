from eb_fast_api.service.jwt.sources.token_service import verifyToken
import pytest
from fastapi import HTTPException


def test_verifyToken_SUCCESS(realJWTService):
    # given
    email = "test@test.com" * 3
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
