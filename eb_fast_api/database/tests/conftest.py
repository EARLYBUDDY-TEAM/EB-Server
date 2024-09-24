import pytest
from eb_fast_api.database.testings.mock_database import (
    mockCommitInBaseCRUD,
    getMockCRUD,
)
from eb_fast_api.database.testings.mock_connection import mockEngine, mockSessionMaker
from eb_fast_api.database.sources.connection import checkConnection
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.sources.model.models import Base


@pytest.fixture(scope="session")
def prepareTestDataBase():
    checkConnection(engine=mockEngine)
    print("Success Connect to DB")

    Base.metadata.create_all(bind=mockEngine)
    print("Success Create Table")

    mockCommitInBaseCRUD()


@pytest.fixture(scope="function")
def mockSession(prepareTestDataBase):
    session = mockSessionMaker()
    print("Create Session !!!")

    yield session

    session.close()
    print("Close Session !!!")


@pytest.fixture(scope="function")
def mockPlaceCRUD(mockSession):
    db = EBDataBase.place
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
    )


@pytest.fixture(scope="function")
def mockUserCRUD(mockSession):
    db = EBDataBase.user
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
    )


@pytest.fixture(scope="function")
def mockScheduleCRUD(mockSession):
    db = EBDataBase.schedule
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
    )
