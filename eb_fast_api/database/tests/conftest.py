import pytest
from eb_fast_api.database.testings.mock_database import (
    mockCommitInBaseCRUD,
    getMockCRUD,
)
from eb_fast_api.database.testings.mock_connection import mockEngine, mockSessionMaker
from eb_fast_api.database.sources.connection import checkConnection
from eb_fast_api.database.sources.database import EBDataBase


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
    yield from getMockCRUD(
        mockSession=mockSession,
        mockEngine=mockEngine,
        db=EBDataBase.place,
    )


@pytest.fixture(scope="function")
def mockUserCRUD(mockSession):
    yield from getMockCRUD(
        mockSession=mockSession,
        mockEngine=mockEngine,
        db=EBDataBase.user,
    )


@pytest.fixture(scope="function")
def mockScheduleCRUD(mockSession):
    yield from getMockCRUD(
        mockSession=mockSession,
        mockEngine=mockEngine,
        db=EBDataBase.schedule,
    )
