from enum import Enum
from sqlalchemy import Engine
from eb_fast_api.database.sources.connection import (
    engine,
    sessionMaker,
    checkConnection,
)
from eb_fast_api.database.sources.model.models import Base, User, Schedule
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
)
from eb_fast_api.env.sources.env import ENV_TEST_USER
from eb_fast_api.snippets.sources import pwdcrypt
from datetime import datetime


class EBDataBase(Enum):
    base = "base"
    user = "user"
    schedule = "schedule"
    place = "place"

    # session 파라미터 타입지정했는데 왜 오류????
    def createCRUD(self, session=sessionMaker()):
        match self:
            case EBDataBase.user:
                return UserCRUD(session)
            case EBDataBase.schedule:
                return ScheduleCRUD(session)
            case EBDataBase.place:
                return PlaceCRUD(session)

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
        name = ENV_TEST_USER.name

        fetchedUser = userCRUD.read(email=email)
        if fetchedUser == None:
            hashedPassword = pwdcrypt.hash(password=ENV_TEST_USER.password)
            testUser = User(
                name=name,
                email=email,
                hashedPassword=hashedPassword,
                refreshToken="",
            )
            userCRUD.create(user=testUser)

        scheduleCRUD = EBDataBase.schedule.createCRUD(session=session)
        for i in range(10):
            mockSchedule = Schedule(
                title=f"index : {i}, {name}'s mock schedule",
                time=datetime.now(),
                isNotify=False,
            )
            scheduleCRUD.create(
                userEmail=email,
                schedule=mockSchedule,
                startPlace=None,
                endPlace=None,
            )
            print(f"Create Mock Schedule, index : {i}")

        session.commit()
        session.close()
        del userCRUD
        del scheduleCRUD


if __name__ == "__main__":
    EBDataBase.initialize()
