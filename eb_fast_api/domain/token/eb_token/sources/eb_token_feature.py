from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from eb_fast_api.service.jwt.sources.jwt_service import jwtService, JWTService
from eb_fast_api.domain.schema.sources.schemas import TokenInfo
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.snippets.sources.logger import logger


def update_refresh_token(
    userCRUD: UserCRUD,
    email: str,
    refreshToken: str,
):
    userCRUD.update(
        key_email=email,
        refreshToken=refreshToken,
    )
    userCRUD.commit()


def create_token_info(
    email: str,
    jwt_service: JWTService,
) -> TokenInfo:
    accessToken = jwt_service.createAccessToken(email=email)
    refreshToken = jwt_service.createRefreshToken(email=email)
    return TokenInfo(
        accessToken=accessToken,
        refreshToken=refreshToken,
    )


def verifyToken(
    token: str,
    fail_status_code: int = 490,
    fail_detail: str = "토큰 만료",
) -> str:
    email = jwtService.checkTokenExpired(token)
    if email == None:
        raise HTTPException(
            status_code=fail_status_code,
            detail=fail_detail,
        )
    else:
        return email


def getUserEmail(
    token=Security(
        APIKeyHeader(name="access-token"),
    )
) -> str:
    return verifyToken(token)
