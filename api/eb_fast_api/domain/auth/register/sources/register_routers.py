from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.domain.schema.sources.schema import UserInfo


router = APIRouter(prefix="/auth/register")


@router.post("")
def register(
    registerInfo: UserInfo,
    db=Depends(getDB),
):
    if not register_feature.isValidEmail(
        registerInfo.email
    ) or not register_feature.isValidPassword(registerInfo.password):
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 올바르지 않습니다.",
        )

    tmpUser = db.userRead(registerInfo.email)
    if tmpUser:
        raise HTTPException(
            status_code=401,
            detail="이미 존재하는 사용자입니다.",
        )
    user = registerInfo.toUser()
    db.userCreate(user)
    db.commit()
