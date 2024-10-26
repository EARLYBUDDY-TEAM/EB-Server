from enum import Enum
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from uuid import uuid4

from eb_fast_api.database.sources.connection import (
    engine,
    sessionMaker,
    checkConnection,
)
from eb_fast_api.database.sources.model.models import Base, User, Schedule, Place, Path
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
    PathCRUD,
)
from eb_fast_api.env.sources.env import ENV_TEST_USER
from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.database.sources import dummy


class EBDataBase(Enum):
    base = "base"
    user = "user"
    schedule = "schedule"
    place = "place"
    path = "path"

    # session 파라미터 타입지정했는데 왜 오류????
    def createCRUD(self, session=sessionMaker()):
        match self:
            case EBDataBase.user:
                return UserCRUD(session)
            case EBDataBase.schedule:
                return ScheduleCRUD(session)
            case EBDataBase.place:
                return PlaceCRUD(session)
            case EBDataBase.path:
                return PathCRUD(session)

    def getCRUD(self):
        session = sessionMaker()
        crud = self.createCRUD(session)
        try:
            yield crud
        finally:
            session.close()
            del crud

    @classmethod
    def create_session(cls) -> Session:
        return sessionMaker()

    @classmethod
    def get_session(cls):
        session = EBDataBase.create_session()
        try:
            yield session
        finally:
            session.close()

    @classmethod
    def __create_meta_data(
        cls,
        engine: Engine,
    ):
        checkConnection(engine=engine)
        print("Success Connect to DB")

        Base.metadata.create_all(bind=engine)
        print("Success Create Table")

    @classmethod
    def __create_test_user(
        cls,
        session: Session,
    ) -> str:
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

        return email

    @classmethod
    def __create_place(
        cls,
        session: Session,
        place: Place,
    ):
        placeCRUD = EBDataBase.place.createCRUD(session=session)
        placeCRUD.create(place=place)

    @classmethod
    def __create_schedule(
        cls,
        session: Session,
        user_email: str,
        schedule: Schedule,
    ):
        scheduleCRUD = EBDataBase.schedule.createCRUD(session=session)
        scheduleCRUD.create(
            userEmail=user_email,
            schedule=schedule,
        )

    @classmethod
    def __create_path(
        cls,
        session: Session,
        user_email: str,
        schedule_id: str,
    ):
        pathCRUD = EBDataBase.path.createCRUD(session=session)
        path = Path(
            id=schedule_id,
            data=dummy.path_data,
        )
        pathCRUD.create(
            user_email=user_email,
            path=path,
        )

    @classmethod
    def initialize(
        cls,
        engine: Engine = engine,
    ):
        EBDataBase.__create_meta_data(engine=engine)

        session = sessionMaker()
        user_email = EBDataBase.__create_test_user(session=session)

        startPlace = Place.mockStart()
        endPlace = Place.mockEnd()
        EBDataBase.__create_place(session=session, place=startPlace)
        EBDataBase.__create_place(session=session, place=endPlace)

        today = datetime.now() + timedelta(minutes=20)
        for i in range(1, 11):
            mockSchedule1 = Schedule(
                id=str(uuid4()),
                title=f"index : {i}, testuser mock schedule",
                memo="This is Memo",
                time=today + timedelta(days=i),
                isNotify=False,
                startPlaceID=startPlace.id,
                endPlaceID=endPlace.id,
            )
            EBDataBase.__create_schedule(
                session=session,
                user_email=user_email,
                schedule=mockSchedule1,
            )
            EBDataBase.__create_path(
                session=session,
                user_email=user_email,
                schedule_id=mockSchedule1.id,
            )

            mockSchedule2 = Schedule(
                id=str(uuid4()),
                title=f"index : {i}, testuser mock schedule",
                memo="This is Memo",
                time=today + timedelta(minutes=10),
                isNotify=False,
                startPlaceID=startPlace.id,
                endPlaceID=endPlace.id,
            )
            EBDataBase.__create_schedule(
                session=session,
                user_email=user_email,
                schedule=mockSchedule2,
            )
            EBDataBase.__create_path(
                session=session,
                user_email=user_email,
                schedule_id=mockSchedule2.id,
            )

        session.commit()
        session.close()


if __name__ == "__main__":
    EBDataBase.initialize()
