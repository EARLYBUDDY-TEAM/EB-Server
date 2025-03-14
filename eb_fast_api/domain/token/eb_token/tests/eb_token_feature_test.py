import pytest
from fastapi import HTTPException
from eb_fast_api.domain.token.eb_token.sources.eb_token_feature import verifyToken


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
