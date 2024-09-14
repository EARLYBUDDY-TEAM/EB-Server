from unittest.mock import patch
from sqlalchemy.orm import Session
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
    db: EBDataBase,
):
    mockCRUD = db.getCRUD(session=mockSession)
    print(f"Create {db.value.capitalize()}CRUD !!!")

    yield mockCRUD

    mockCRUD.rollback()
    print(f"Rollback {db.value.capitalize()}CRUD !!!")

    del mockCRUD
    print(f"Del {db.value.capitalize()}CRUD")
