from fastapi import APIRouter, HTTPException

from eb_fast_api.domain.auth.register.sources import register_schema
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.database.sources import db_crud
from eb_fast_api.database.sources.models import User

router = APIRouter(prefix="/auth/register")

@router.post("/")
def user_create(registerInfo: register_schema.RegisterInfo):
    if not register_feature.is_valid_email(
        registerInfo.email
    ) or not register_feature.is_valid_password(registerInfo.password):
        raise HTTPException(
            status_code = 400,
            detail = "유저 정보가 올바르지 않습니다.",
        )
    
    tmpUser = db_crud.user_read(registerInfo.email)
    if tmpUser:
        raise HTTPException(
            status_code = 401,
            detail = "이미 존재하는 사용자입니다.",
        )
    hashedPassword = register_feature.hash_password(registerInfo.password)
    user = User(email = registerInfo.email, password = hashedPassword)
    db_crud.user_create(user)
