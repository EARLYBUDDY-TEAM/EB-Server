from unittest.mock import patch
from sqlalchemy.orm import Session
from sqlalchemy import Engine
from typing import Any
from eb_fast_api.database.sources.crud.cruds import PlaceCRUD, UserCRUD, ScheduleCRUD
from eb_fast_api.database.sources.database import EBDataBase


def mockCommitInBaseCRUD():
    def mockCommit(self):
        print("This is mock commit")
        return

    patcher = patch(
        "eb_fast_api.database.sources.crud.base_crud.BaseCRUD.commit", new=mockCommit
    )
    patcher.start()


def getMockCRUD(
    mockSession: Session,
    mockEngine: Engine,
    db: EBDataBase,
):
    db.createTable(engine=mockEngine)

    mockCRUD: Any
    match db:
        case EBDataBase.user:
            mockCRUD = UserCRUD(mockSession)
        case EBDataBase.schedule:
            mockCRUD = ScheduleCRUD(mockSession)
        case EBDataBase.place:
            mockCRUD = PlaceCRUD(mockSession)
    print("Create MockCRUD !!!")

    yield mockCRUD

    mockCRUD.rollback()
    print("Rollback MockCRUD !!!")

    del mockCRUD
    print("Del MockCRUD")
