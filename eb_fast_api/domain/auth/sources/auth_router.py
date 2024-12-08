from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import TokenInfo, LoginInfo, RegisterInfo
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.auth.sources.auth_feature import login_feature
from eb_fast_api.domain.auth.sources.auth_feature import register_feature


router = APIRouter(prefix="/auth")


@router.post("/login")
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


@router.post("/register")
def register(
    registerInfo: RegisterInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
    if not register_feature.isValidRegisterInfo(registerInfo):
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 올바르지 않습니다.",
        )

    try:
        register_feature.createUser(
            registerInfo=registerInfo,
            userCRUD=userCRUD,
        )
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )
