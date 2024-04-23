from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

# from database.database import get_db
# from domain.user import user_schema
# from domain.user import user_feature
# from domain.model.default_response import DefaultResponse


router = APIRouter(prefix="/user")

@router.post("/create")
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    return DefaultResponse(isSuccess=True)

# @router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
# def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    # user = user_feature.get_existing_user(db, user_create=_user_create)
    # if user:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail="이미 존재하는 사용자입니다.",
    #     )
    # user_feature.create_user(db=db, user_create=_user_create)
    # return DefaultResponse(isSuccess=True)