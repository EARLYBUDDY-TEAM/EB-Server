from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
import secrets

from eb_server.database.database import get_db
from eb_server.domain.auth.login.sources import login_feature
from eb_server.domain.auth.login.sources import login_schema

ACCESS_TOKEN_EXPIRE_MINUTES = 10
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=login_schema.Token)
def login_for_access_token(
    _login_info: login_schema.LoginInfo, db: Session = Depends(get_db)
):
    user = login_feature.get_user(db, _login_info.email)

    if not (
        user
        and login_feature.check_password(
            password=_login_info.password, hashed_password=user.password
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="잘못된 유저정보 또는 패스워드입니다.",
            headers={"WWW-Authenticate": "Bearer"},
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

# {
#   "email": "abcd@naver.com",
#   "password": "password"
# }

# {
#   "email": "abc@naver.com",
#   "password": "password12"
# }