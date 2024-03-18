from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate
from database.models import User

from fastapi import APIRouter

app = APIRouter(
    prefix="/auth",
)

def create_user(db: Session, user_create: UserCreate):
    db_user = User(
        email = user_create.email,
        password = user_create.password1
        )
    db.add(db_user)
    db.commit()