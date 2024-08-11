from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.snippets.pwdcrypt.sources import pwdcrypt
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.auth.login.sources.login_schema import Token
from eb_fast_api.domain.schema.sources.schema import UserInfo

from eb_fast_api.snippets.jwt_service.sources.jwt_service import JWTService


router = APIRouter(prefix="/auth/login")


@router.post('', response_model=Token)
def login(loginInfo: UserInfo, db = Depends(getDB)):
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
    
    jwtService = JWTService()
    accessToken = jwtService.createAccessToken(user.email)
    refreshToken = jwtService.createRefreshToken(user.email)

    return Token(
        accessToken, refreshToken
    )
