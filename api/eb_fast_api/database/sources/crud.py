from sqlalchemy.orm import Session
from typing import Optional
from eb_fast_api.database.sources.models import User, Schedule, Place
from eb_fast_api.database.sources.database import sessionMaker
from eb_fast_api.snippets.sources import pwdcrypt



class CRUD():
    session: Session

    def __init__(self, session: Session):
        self.session = session

        # db
    def rollback(self):
        self.session.rollback()


    def commit(self):
        self.session.commit()

    # user
    def userCreate(self, user: User):
        self.session.add(user)
        self.session.flush()


    def userRead(self, email: str) -> User:
        user = self.session.query(User).filter(User.email == email).first()
        return user


    # schedule
    def scheduleCreate(
        self,
        userEmail: str,
        schedule: Schedule,
        startPlace: Optional[Place],
        endPlace: Optional[Place],
    ):
        user = self.session.query(User).filter(User.email == userEmail).first()
        if not user:
            raise Exception("no user")
        
        if startPlace is not None:
            self.placeCreate(startPlace)
        if endPlace is not None:
            self.placeCreate(endPlace)

        user.schedules.append(schedule)  # 중복체크?
        self.session.flush()


    # place
    def placeRead(self, placeID: str) -> Place:
        place = self.session.query(Place).filter(Place.id == placeID).first()
        return place


    def placeCreate(self, place: Place):
        fetchedPlace = self.placeRead(place.id)
        if not fetchedPlace:
            self.session.add(place)
            self.session.flush()


def getDB():
    session = sessionMaker()
    crud = CRUD(session = session)
    try:
        yield crud
    finally:
        session.close()
        del crud