from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schema import RegisterInfo


router = APIRouter(prefix="/auth/register")


@router.post("")
def register(
    registerInfo: RegisterInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
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

    user = registerInfo.toUser(refreshToken="")
    userCRUD.create(user)
    userCRUD.commit()
