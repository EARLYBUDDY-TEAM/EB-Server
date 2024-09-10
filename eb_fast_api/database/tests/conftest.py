import pytest
from eb_fast_api.database.testings.mock_crud import (
    mockCommitInBaseCRUD,
    mockSessionMaker,
    mockEngine,
)
from eb_fast_api.database.sources.connection import checkConnection
from eb_fast_api.database.sources.database import EBDatabase
from eb_fast_api.database.sources.crud.cruds import PlaceCRUD, UserCRUD, ScheduleCRUD


@pytest.fixture(scope="session")
def mockCommit():
    mockCommitInBaseCRUD()
    print("start test session")
    yield
    print("finish test session")


@pytest.fixture(scope="session")
def mockSession():
    checkConnection(engine=mockEngine)
    print("Success Connect to DB")

    mockCommitInBaseCRUD()

    session = mockSessionMaker()
    print("Create Session !!!")

    yield session

    session.close()
    print("Close Session !!!")


@pytest.fixture(scope="function")
def mockPlaceCRUD(mockSession):
    EBDatabase.place.createTable(engine=mockEngine)

    crudPlace = PlaceCRUD(session=mockSession)
    print("Create PlaceCRUD !!!")

    yield crudPlace

    crudPlace.rollback()
    print("Rollback PlaceCRUD !!!")

    del crudPlace
    print("Del PlaceCRUD")


@pytest.fixture(scope="function")
def mockUserCRUD(mockSession):
    EBDatabase.user.createTable(engine=mockEngine)

    userCRUD = UserCRUD(session=mockSession)
    print("Create UserCRUD !!!")

    yield userCRUD

    userCRUD.rollback()
    print("Rollback UserCRUD !!!")

    del userCRUD
    print("Del UserCRUD")


@pytest.fixture(scope="function")
def mockScheduleCRUD(mockSession):
    EBDatabase.schedule.createTable(engine=mockEngine)

    scheduleCRUD = ScheduleCRUD(session=mockSession)
    print("Create ScheduleCRUD !!!")

    yield scheduleCRUD

    scheduleCRUD.rollback()
    print("Rollback ScheduleCRUD !!!")

    del scheduleCRUD
    print("Del ScheduleCRUD")
