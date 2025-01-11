from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import LoginInfo, RegisterInfo
from eb_fast_api.domain.auth.sources.auth_schema import ChangePasswordInfo, LoginResult
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.domain.auth.sources.auth_feature import (
    delete_user_feature,
    login_feature,
    register_feature,
    change_password_feature,
)
from eb_fast_api.domain.token.eb_token.sources.eb_token_feature import getUserEmail
from eb_fast_api.snippets.sources import dictionary


router = APIRouter(prefix="/auth")


@router.post("/login")
def login(
    loginInfo: LoginInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> LoginResult:
    try:
        user = login_feature.check_password(
            user_crud=userCRUD,
            login_info=loginInfo,
        )
        nick_name = dictionary.safeDict(keyList=["nickName"], fromDict=user) or ""
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

        return LoginResult(
            nick_name=nick_name,
            token_info=token_info,
        )

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
    if register_feature.is_exist_user(
        userCRUD=userCRUD,
        email=registerInfo.email,
    ):
        raise HTTPException(
            status_code=401,
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
            status_code=402,
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


@router.delete("/delete_user")
def delete_user(
    user_email=Depends(getUserEmail),
    user_crud=Depends(EBDataBase.user.getCRUD),
    def_create_engine=Depends(EBDataBase.get_def_create_engine),
):
    try:
        delete_user_feature.delete_user_data_in_db(
            user_email=user_email,
            user_crud=user_crud,
            def_create_engine=def_create_engine,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400,
            detail="유저 삭제에 실패했습니다.",
        )
