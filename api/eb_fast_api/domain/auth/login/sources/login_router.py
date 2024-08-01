from fastapi import APIRouter, HTTPException

from eb_fast_api.domain.auth.login.sources.login_schema import LoginInfo, Token
from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.database.sources import db_crud
from eb_fast_api.snippets.sources import password


from eb_fast_api.database.sources.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session


router = APIRouter(prefix="/auth/login")


@router.post('', response_model=Token)
def login_for_access_token(login_info: LoginInfo, session: Session = Depends(get_db)):
    user = db_crud.user_read(login_info.email, session)

    if not user:
        raise HTTPException(
            status_code = 400,
            detail = '유저정보가 없습니다.',
        )
    
    if not password.check(
        password = login_info.password, 
        hashed_password = user.password
    ):
        raise HTTPException(
            status_code = 401,
            detail = '잘못된 패스워드 입니다.',
        )

    access_token = login_feature.create_token(user.email)

    return Token(
        access_token=access_token,
        token_type="bearer",
        email=user.email,
    )
