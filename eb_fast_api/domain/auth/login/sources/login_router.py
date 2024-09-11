from fastapi import APIRouter, HTTPException
from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schema import Token, UserInfo
from eb_fast_api.service.jwt.sources.jwt_service import jwtService


router = APIRouter(prefix="/auth/login")


@router.post("")
def login(
    loginInfo: UserInfo,
    userCRUD=EBDataBase.user.depends(),
) -> Token:
    user = userCRUD.read(loginInfo.email)

    if not user:
        raise HTTPException(
            status_code=400,
            detail="유저정보가 없습니다.",
        )

    if not pwdcrypt.check(
        password=loginInfo.password, hashedPassword=user.hashedPassword
    ):
        raise HTTPException(
            status_code=401,
            detail="잘못된 패스워드 입니다.",
        )

    accessToken = jwtService.createAccessToken(user.email)
    refreshToken = jwtService.createRefreshToken(user.email)

    return Token(accessToken, refreshToken)
