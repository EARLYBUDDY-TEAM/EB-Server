from eb_fast_api.database.sources.models import User, Schedule
from eb_fast_api.database.sources.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session


def rollback(
    session: Session = Depends(get_db),
):
    session.rollback()


def user_create(
    user: User,
    session: Session = Depends(get_db),
):
    session.add(user)
    session.flush()


def user_read(
    email: str,
    session: Session = Depends(get_db),
) -> User:
    user = session.query(User).filter(User.email == email).first()
    return user


def schedule_create(
    userEmail: str,
    schedule: Schedule,
    session: Session = Depends(get_db),
):
    user = session.query(User).filter(User.email == userEmail).first()
    if not user:
        raise Exception('no user')
    user.schedules.append(schedule) # 중복체크?
    session.flush()