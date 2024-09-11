from enum import Enum
from sqlalchemy import inspect, Engine
from sqlalchemy.orm import Session
from typing import Any
from eb_fast_api.database.sources.connection import engine, sessionMaker
from eb_fast_api.database.sources.model.models import User, Schedule, Place
from eb_fast_api.database.sources.crud.cruds import (
    PlaceCRUD,
    ScheduleCRUD,
    UserCRUD,
)


class EBDataBase(Enum):
    user = "User"
    schedule = "Schedule"
    place = "Place"

    # sessionMaker 타입지정했는데 왜 오류????
    def getCRUD(self, sessionMaker=sessionMaker):
        session: Session = sessionMaker()
        crud: Any
        match self:
            case EBDataBase.user:
                crud = UserCRUD(session)
            case EBDataBase.schedule:
                crud = ScheduleCRUD(session)
            case EBDataBase.place:
                crud = PlaceCRUD(session)
        try:
            yield crud
        finally:
            session.close()
            del crud

    def createTable(self, engine: Engine = engine):
        if inspect(engine).has_table(self.value):
            print("Exist Table ...")
            return

        EB_Table: Any
        match self:
            case EBDataBase.user:
                EB_Table = User
            case EBDataBase.schedule:
                EB_Table = Schedule
            case EBDataBase.place:
                EB_Table = Place

        EB_Table.__table__.create(bind=engine, checkfirst=True)
