from enum import Enum
from sqlalchemy import inspect, Engine
from sqlalchemy.orm import Session
from typing import Any
from eb_fast_api.database.sources.connection import engine, sessionMaker
from eb_fast_api.database.sources.model.models import User, Schedule, Place
from eb_fast_api.database.sources.crud.cruds import PlaceCRUD, ScheduleCRUD, UserCRUD


class EBDatabase(Enum):
    user = "User"
    schedule = "Schedule"
    place = "Place"

    def getCRUD(self, session: Session = sessionMaker()):
        EB_CRUD: Any
        if self == EBDatabase.user:
            EB_CRUD = UserCRUD
        elif self == EBDatabase.schedule:
            EB_CRUD = ScheduleCRUD
        elif self == EBDatabase.place:
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
        if self == EBDatabase.user:
            EB_Table = User
        elif self == EBDatabase.schedule:
            EB_Table = Schedule
        elif self == EBDatabase.place:
            EB_Table = Place

        EB_Table.__table__.create(bind=engine, checkfirst=True)
