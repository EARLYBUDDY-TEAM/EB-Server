from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
import secrets

from eb_fast_api.database.database import get_db
from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.domain.auth.login.sources import login_schema

ACCESS_TOKEN_EXPIRE_MINUTES = 10
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth/login")

@router.post("/", response_model=login_schema.Token)
def login_for_access_token(
    _login_info: login_schema.LoginInfo, db: Session = Depends(get_db)
):
    user = login_feature.get_user(db, _login_info.email)

    if not user:
        raise HTTPException(
            status_code = 400,
            detail = '유저정보가 없습니다.',
        )
    
    if not login_feature.check_password(
        password = _login_info.password, 
        hashed_password = user.password
    ):
        raise HTTPException(
            status_code = 401,
            detail = '잘못된 패스워드 입니다.',
        )

    data = {
        "sub": user.email,
        "exp" : datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return login_schema.Token(
        access_token=access_token,
        token_type="bearer",
        email=user.email,
    )
