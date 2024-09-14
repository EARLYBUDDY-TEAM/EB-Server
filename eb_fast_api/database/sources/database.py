from enum import Enum
from sqlalchemy import inspect, Engine
from eb_fast_api.database.sources.connection import engine, sessionMaker
from eb_fast_api.database.sources.model.models import Base
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
)


class EBDataBase(Enum):
    base = "base"
    user = "user"
    schedule = "schedule"
    place = "place"

    # session 파라미터 타입지정했는데 왜 오류????
    def getCRUD(self, session):
        match self:
            case EBDataBase.user:
                return UserCRUD(session)
            case EBDataBase.schedule:
                return ScheduleCRUD(session)
            case EBDataBase.place:
                return PlaceCRUD(session)

    def getUserCRUD(self, session=sessionMaker()):
        crud = self.getCRUD(session)
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
        Base.metadata.create_all(bind=engine)
        # mixinSchedule = Schedule.mixinClass(email=ENV_TEST_USER.email)
        # Base.metadata.create_all(bind=engine)
        # userCRUD = EBDataBase.user.getCRUD(session=session)
        # userCRUD.create(user=)
