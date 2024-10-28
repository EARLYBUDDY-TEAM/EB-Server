from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import TokenInfo, LoginInfo
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService


router = APIRouter(prefix="/auth/login")


@router.post("")
def login(
    loginInfo: LoginInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> TokenInfo:
    user = userCRUD.read(email=loginInfo.email)

    if not user:
        raise HTTPException(
            status_code=400,
            detail="유저정보가 없습니다.",
        )

    if not pwdcrypt.check(
        password=loginInfo.password,
        hashedPassword=user["hashedPassword"],
    ):
        raise HTTPException(
            status_code=401,
            detail="잘못된 패스워드 입니다.",
        )

    email = user["email"]
    accessToken = jwtService.createAccessToken(email)
    refreshToken = jwtService.createRefreshToken(email)

    userCRUD.update(
        key_email=loginInfo.email,
        refreshToken=refreshToken,
    )
    userCRUD.commit()

    return TokenInfo(
        accessToken=accessToken,
        refreshToken=refreshToken,
    )
