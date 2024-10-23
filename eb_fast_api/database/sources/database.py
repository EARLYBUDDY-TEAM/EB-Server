from enum import Enum
from sqlalchemy import Engine
from eb_fast_api.database.sources.connection import (
    engine,
    sessionMaker,
    checkConnection,
)
from eb_fast_api.database.sources.model.models import Base, User, Schedule, Place
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
    RouteCRUD,
)
from eb_fast_api.env.sources.env import ENV_TEST_USER
from eb_fast_api.snippets.sources import pwdcrypt
from datetime import datetime, timedelta


class EBDataBase(Enum):
    base = "base"
    user = "user"
    schedule = "schedule"
    place = "place"
    route = "route"

    # session 파라미터 타입지정했는데 왜 오류????
    def createCRUD(self, session=sessionMaker()):
        match self:
            case EBDataBase.user:
                return UserCRUD(session)
            case EBDataBase.schedule:
                return ScheduleCRUD(session)
            case EBDataBase.place:
                return PlaceCRUD(session)
            case EBDataBase.route:
                return RouteCRUD(session)

    def getCRUD(self):
        session = sessionMaker()
        crud = self.createCRUD(session)
        try:
            yield crud
        finally:
            session.close()
            del crud

    @classmethod
    def initialize(
        self,
        engine: Engine = engine,
    ):
        checkConnection(engine=engine)
        print("Success Connect to DB")

        Base.metadata.create_all(bind=engine)
        print("Success Create Table")

        session = sessionMaker()
        userCRUD = EBDataBase.user.createCRUD(session=session)
        email = ENV_TEST_USER.email
        nickName = ENV_TEST_USER.nick_name

        fetchedUser = userCRUD.read(email=email)
        if fetchedUser == None:
            hashedPassword = pwdcrypt.hash(password=ENV_TEST_USER.password)
            testUser = User(
                nickName=nickName,
                email=email,
                hashedPassword=hashedPassword,
                refreshToken="",
            )
            userCRUD.create(user=testUser)

        startPlace = Place.mockStart()
        endPlace = Place.mockEnd()
        placeCRUD = EBDataBase.place.createCRUD(session=session)
        placeCRUD.create(place=startPlace)
        placeCRUD.create(place=endPlace)

        scheduleCRUD = EBDataBase.schedule.createCRUD(session=session)
        today = datetime.now() + timedelta(minutes=20)
        for i in range(1, 11):
            mockSchedule1 = Schedule(
                title=f"index : {i}, {nickName}'s mock schedule",
                memo="This is Memo",
                time=today + timedelta(days=i),
                isNotify=False,
                startPlaceID=startPlace.id,
                endPlaceID=endPlace.id,
            )
            scheduleCRUD.create(
                userEmail=email,
                schedule=mockSchedule1,
            )

            mockSchedule2 = Schedule(
                title=f"index : {i}, {nickName}'s mock schedule",
                memo="This is Memo",
                time=today + timedelta(minutes=10),
                isNotify=False,
                startPlaceID=startPlace.id,
                endPlaceID=endPlace.id,
            )
            scheduleCRUD.create(
                userEmail=email,
                schedule=mockSchedule2,
            )

        session.commit()
        session.close()
        del userCRUD
        del placeCRUD
        del scheduleCRUD


if __name__ == "__main__":
    EBDataBase.initialize()
