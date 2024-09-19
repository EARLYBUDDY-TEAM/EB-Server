from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.domain.schema.sources.schema import UserInfo, Token
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService


router = APIRouter(prefix="/auth/register")


@router.post("")
def register(
    registerInfo: UserInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
    jwtService=Depends(getJWTService),
) -> Token:
    if not register_feature.isValidEmail(
        registerInfo.email
    ) or not register_feature.isValidPassword(registerInfo.password):
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 올바르지 않습니다.",
        )

    tmpUser = userCRUD.read(registerInfo.email)
    if tmpUser:
        raise HTTPException(
            status_code=401,
            detail="이미 존재하는 사용자입니다.",
        )

    accessToken = jwtService.createAccessToken(email=registerInfo.email)
    refreshToken = jwtService.createRefreshToken(email=registerInfo.email)
    token = Token(
        accessToken=accessToken,
        refreshToken=refreshToken,
    )

    user = registerInfo.toUser(refreshToken=refreshToken)
    userCRUD.create(user)
    userCRUD.commit()

    return token
