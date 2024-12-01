from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import TokenInfo, LoginInfo
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.auth.login.sources import login_feature


router = APIRouter(prefix="/auth/login")


@router.post("")
def login(
    loginInfo: LoginInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> TokenInfo:
    try:
        user = login_feature.check_password(
            user_crud=userCRUD,
            login_info=loginInfo,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    token_info = login_feature.create_auth_token(
        user=user,
        jwtService=jwtService,
    )

    try:
        login_feature.update_tokens(
            user_crud=userCRUD,
            token_info=token_info,
            login_info=loginInfo,
        )
        return token_info
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401,
            detail="토큰 업데이트에 실패했습니다.",
        )
