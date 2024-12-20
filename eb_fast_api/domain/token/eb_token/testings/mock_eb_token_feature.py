from unittest.mock import patch
from fastapi.security import APIKeyHeader
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from eb_fast_api.domain.schema.sources.schemas import TokenInfo
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.domain.token.eb_token.sources import eb_token_feature


def patcher_update_refresh_token_SUCCESS():
    return patch.object(
        eb_token_feature,
        "update_refresh_token",
        return_value=None,
    )


def patcher_update_refresh_token_FAIL():
    def raise_exception(
        userCRUD: UserCRUD,
        email: str,
        refreshToken: str,
    ):
        raise Exception()

    return patch.object(
        eb_token_feature,
        "update_refresh_token",
        new=raise_exception,
    )


def patcher_verifyToken_SUCCESS(email: str):
    return patch.object(
        eb_token_feature,
        "verifyToken",
        return_value=email,
    )


def patcher_verifyToken_FAIL():
    def raise_exception(
        token: str,
        fail_status_code: int = 490,
        fail_detail: str = "토큰 만료",
    ):
        raise HTTPException(
            status_code=fail_status_code,
            detail=fail_detail,
        )

    return patch.object(
        eb_token_feature,
        "verifyToken",
        new=raise_exception,
    )


def patcher_create_token_info(tokenInfo: TokenInfo):
    return patch.object(
        eb_token_feature,
        "create_token_info",
        return_value=tokenInfo,
    )


mockEmail = "test@test.com"


def mockGetUserEmail(
    token=Security(
        APIKeyHeader(name="access_token"),
    )
) -> str:
    return mockEmail
