from fastapi import APIRouter, HTTPException, Depends

from eb_fast_api.domain.auth.register.sources import register_schema
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.database.sources.models import User
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.snippets.sources import pwdcrypt

router = APIRouter(prefix="/auth/register")

@router.post("/")
def user_create(registerInfo: register_schema.RegisterInfo, db = Depends(getDB)):
    if not register_feature.is_valid_email(
        registerInfo.email
    ) or not register_feature.is_valid_password(registerInfo.password):
        raise HTTPException(
            status_code = 400,
            detail = "유저 정보가 올바르지 않습니다.",
        )
    
    tmpUser = db.user_read(registerInfo.email)
    if tmpUser:
        raise HTTPException(
            status_code = 401,
            detail = "이미 존재하는 사용자입니다.",
        )
    hashedPassword = pwdcrypt.hash(registerInfo.password)
    user = User(email = registerInfo.email, password = hashedPassword)
    db.user_create(user)
