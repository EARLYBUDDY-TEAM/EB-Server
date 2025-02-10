from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader
from eb_fast_api.domain.token.eb_token.sources import eb_token_feature
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.schema.sources.schemas import TokenInfo


router = APIRouter(prefix="/token/eb")


@router.get("/recreate")
def recreate_token(
    refreshToken=Security(
        APIKeyHeader(name="refresh-token"),
    ),
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> TokenInfo:
    userEmail = eb_token_feature.verifyToken(token=refreshToken)
    token_info = eb_token_feature.create_token_info(
        email=userEmail,
        jwt_service=jwtService,
    )

    try:
        eb_token_feature.update_refresh_token(
            userCRUD=userCRUD,
            email=userEmail,
            refreshToken=token_info.refreshToken,
        )
        return token_info
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=491,
            detail="토큰 저장 실패",
        )
