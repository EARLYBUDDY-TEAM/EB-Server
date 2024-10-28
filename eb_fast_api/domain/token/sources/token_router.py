from fastapi import APIRouter, Depends, Security
from fastapi.security import APIKeyHeader
from eb_fast_api.domain.token.sources.token_feature import verifyToken
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.schema.sources.schemas import TokenInfo


router = APIRouter(prefix="/token")


@router.get("/recreate")
def recreate_token(
    refreshToken=Security(
        APIKeyHeader(name="refresh_token"),
    ),
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> TokenInfo:
    userEmail = verifyToken(token=refreshToken)
    accessToken = jwtService.createAccessToken(email=userEmail)
    refreshToken = jwtService.createRefreshToken(email=userEmail)
    token = TokenInfo(
        accessToken=accessToken,
        refreshToken=refreshToken,
    )

    userCRUD.update(
        key_email=userEmail,
        refreshToken=refreshToken,
    )
    userCRUD.commit()

    return token
