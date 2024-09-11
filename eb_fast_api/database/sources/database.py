from enum import Enum
from sqlalchemy import inspect, Engine
from sqlalchemy.orm import Session
from typing import Any, Annotated
from fastapi import Depends
from eb_fast_api.database.sources.connection import engine, sessionMaker
from eb_fast_api.database.sources.model.models import User, Schedule, Place
from eb_fast_api.database.sources.crud.cruds import PlaceCRUD, ScheduleCRUD, UserCRUD


class EBDataBase(Enum):
    user = "User"
    schedule = "Schedule"
    place = "Place"

    def getCRUD(self, session: Session = sessionMaker()):
        EB_CRUD: Any
        if self == EBDataBase.user:
            EB_CRUD = UserCRUD
        elif self == EBDataBase.schedule:
            EB_CRUD = ScheduleCRUD
        elif self == EBDataBase.place:
            EB_CRUD = PlaceCRUD
        crud = EB_CRUD(session=session)
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
        if self == EBDataBase.user:
            EB_Table = User
        elif self == EBDataBase.schedule:
            EB_Table = Schedule
        elif self == EBDataBase.place:
            EB_Table = Place

        EB_Table.__table__.create(bind=engine, checkfirst=True)

    def depends(self):
        if self == EBDataBase.user:
            return Annotated[UserCRUD, Depends(EBDataBase.user.getCRUD)]
        elif self == EBDataBase.schedule:
            return Annotated[ScheduleCRUD, Depends(EBDataBase.schedule.getCRUD)]
        elif self == EBDataBase.place:
            return Annotated[PlaceCRUD, Depends(EBDataBase.place.getCRUD)]
