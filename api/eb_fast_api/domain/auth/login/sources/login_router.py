from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.auth.login.sources.login_schema import LoginInfo, Token
from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.database.sources.crud import getDB


router = APIRouter(prefix="/auth/login")


@router.post('', response_model=Token)
def login_for_access_token(loginInfo: LoginInfo, db = Depends(getDB)):
    user = db.userRead(loginInfo.email)

    if not user:
        raise HTTPException(
            status_code = 400,
            detail = '유저정보가 없습니다.',
        )
    
    if not pwdcrypt.check(
        password = loginInfo.password,
        hashedPassword = user.hashedPassword
    ):
        raise HTTPException(
            status_code = 401,
            detail = '잘못된 패스워드 입니다.',
        )

    access_token = login_feature.create_token(user.email)

    return Token(
        access_token=access_token,
        token_type="bearer",
        email=user.email,
    )
