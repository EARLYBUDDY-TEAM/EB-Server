from enum import Enum
from sqlalchemy import Engine
from eb_fast_api.database.sources.connection import (
    engine,
    sessionMaker,
    checkConnection,
)
from eb_fast_api.database.sources.model.models import Base, User
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
)
from eb_fast_api.env.sources.env import ENV_TEST_USER
from eb_fast_api.snippets.sources import pwdcrypt


class EBDataBase(Enum):
    base = "base"
    user = "user"
    schedule = "schedule"
    place = "place"

    # session 파라미터 타입지정했는데 왜 오류????
    def createCRUD(self, session):
        match self:
            case EBDataBase.user:
                return UserCRUD(session)
            case EBDataBase.schedule:
                return ScheduleCRUD(session)
            case EBDataBase.place:
                return PlaceCRUD(session)

    def getCRUD(self, session=sessionMaker()):
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

        fetchedUser = userCRUD.read(email=email)
        if fetchedUser != None:
            session.close()
            return

        hashedPassword = pwdcrypt.hash(password=ENV_TEST_USER.password)
        testUser = User(
            email=email,
            hashedPassword=hashedPassword,
            refreshToken="refreshToken",
        )
        userCRUD.create(user=testUser)
        userCRUD.commit()
        session.close()
