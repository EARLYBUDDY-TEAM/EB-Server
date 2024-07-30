from eb_fast_api.database.sources.models import User, Schedule
from fastapi import Depends
from sqlalchemy.orm import Session
from eb_fast_api.database.sources.database import get_db

def db_commit(db: Session = Depends(get_db)):
    db.commit()

def db_rollback(db: Session = Depends(get_db)):
    db.rollback()

def user_create(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.flush()

def user_read(email: str, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.email == email).first()
    return user

def schedule_create():
    return