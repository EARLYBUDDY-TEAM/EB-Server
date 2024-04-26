from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from eb_server.domain.user.features import user_schema
from eb_server.domain.user.features import user_feature
from eb_server.database.database import get_db

router = APIRouter(prefix="/user")

@router.post("/create")
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    if not user_feature.is_valid_email(
        _user_create.email
    ) or not user_feature.is_valid_password(_user_create.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유저 정보가 올바르지 않습니다.",
        )

    user = user_feature.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자입니다.",
        )
    user_feature.create_user(db=db, user_create=_user_create)
    return