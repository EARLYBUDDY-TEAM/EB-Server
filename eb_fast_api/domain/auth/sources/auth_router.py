from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import TokenInfo, LoginInfo, RegisterInfo
from eb_fast_api.domain.auth.sources.auth_schema import ChangePasswordInfo
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.auth.sources.auth_feature import (
    login_feature,
    register_feature,
    change_password_feature,
)
from eb_fast_api.domain.token.sources.token_feature import getUserEmail


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
    tmpUser = userCRUD.read(registerInfo.email)
    if tmpUser:
        raise HTTPException(
            status_code=402,
            detail="이미 존재하는 사용자입니다.",
        )

    if not register_feature.isValidRegisterInfo(
        registerInfo=registerInfo,
    ):
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


@router.post("/change_password")
def change_password(
    register_info: ChangePasswordInfo,
    user_crud=Depends(EBDataBase.user.getCRUD),
):
    password = register_info.password
    if not change_password_feature.isValidPassword(password=password):
        raise HTTPException(
            status_code=400,
            detail="비밀번호가 올바르지 않습니다.",
        )

    try:
        change_password_feature.update_pwd(
            email=register_info.email,
            password=password,
            user_crud=user_crud,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401,
            detail="비밀번호 변경에 실패했습니다.",
        )


@router.delete("/remove_user")
def remove_user(
    user_email=Depends(getUserEmail),
    user_crud=Depends(EBDataBase.user.getCRUD),
):
    try:
        user_crud.delete(email=user_email)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400,
            detail="유저 삭제에 실패했습니다.",
        )
