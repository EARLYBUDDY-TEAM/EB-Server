from eb_fast_api.database.sources.models import User, Schedule, Place
from eb_fast_api.database.sources.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional


# db
def rollback(session: Session = Depends(get_db)):
    session.rollback()


def commit(session: Session = Depends(get_db)):
    session.commit()


# user
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


# schedule
def schedule_create(
    userEmail: str,
    schedule: Schedule,
    startPlace: Optional[Place],
    endPlace: Optional[Place],
    session: Session = Depends(get_db),
):
    user = session.query(User).filter(User.email == userEmail).first()
    if not user:
        raise Exception("no user")
    
    if startPlace is not None:
        place_create(startPlace, session)
    if endPlace is not None:
        place_create(endPlace, session)

    user.schedules.append(schedule)  # 중복체크?
    session.flush()


# place
def place_read(
    placeID: str,
    session: Session = Depends(get_db),
) -> Place:
    place = session.query(Place).filter(Place.id == placeID).first()
    return place


def place_create(
    place: Place,
    session: Session = Depends(get_db),
):
    fetchedPlace = place_read(place.id, session)
    if not fetchedPlace:
        session.add(place)
        session.flush()