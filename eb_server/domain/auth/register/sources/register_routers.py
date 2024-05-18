from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from eb_server.domain.auth.register.sources import register_schema
from eb_server.domain.auth.register.sources import register_feature
from eb_server.database.database import get_db

router = APIRouter(prefix="/auth/register")

@router.post("/")
def user_create(_register_info: register_schema.RegisterInfo, db: Session = Depends(get_db)):
    if not register_feature.is_valid_email(
        _register_info.email
    ) or not register_feature.is_valid_password(_register_info.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유저 정보가 올바르지 않습니다.",
        )

    is_exist = register_feature.is_exist_user(db=db, register_info=_register_info)
    if is_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자입니다.",
        )
    register_feature.create_user(db=db, register_info=_register_info)
    return
