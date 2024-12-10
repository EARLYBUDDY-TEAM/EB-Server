import pytest
from eb_fast_api.database.testings.mock_database import (
    mockCommitInBaseCRUD,
    mock_commit,
    getMockCRUD,
)
from eb_fast_api.database.testings.mock_connection import (
    createdMockEngine,
    mockSessionMaker,
)
from eb_fast_api.database.sources.connection import checkConnection
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.sources.model.models import Base, User, Schedule, Path
from sqlalchemy import Engine


my_mock_user = User.mock()


def dropTable(engine: Engine):
    try:
        print("Start Drop Schedule Table")
        Schedule.dropTable(
            user_email=my_mock_user.email,
            engine=engine,
        )
        print("Success Drop Schedule Table")
    except:
        print("Not Exist Schedule Table")

    try:
        print("Start Drop Path Table")
        Path.dropTable(
            user_email=my_mock_user.email,
            engine=engine,
        )
        print("Success Drop Path Table")
    except:
        print("Not Exist Path Table")


@pytest.fixture(scope="session")
def prepareTestDataBase():
    checkConnection(engine=createdMockEngine)
    print("Success Connect to DB")

    Base.metadata.create_all(bind=createdMockEngine)
    print("Success Create Table")

    mockCommitInBaseCRUD()
    mock_commit()


@pytest.fixture(scope="function")
def mockEngine(prepareTestDataBase):
    engine = createdMockEngine
    print("Create Engine !!!")

    yield engine


@pytest.fixture(scope="function")
def mockSession(mockEngine):
    session = mockSessionMaker()
    print("Create Session !!!")

    yield session

    session.close()
    print("Close Session !!!")

    dropTable(engine=mockEngine)


@pytest.fixture(scope="function")
def mockPlaceCRUD(mockSession, mockEngine):
    db = EBDataBase.place
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
        mockEngine=mockEngine,
    )


@pytest.fixture(scope="function")
def mockUserCRUD(mockSession, mockEngine):
    db = EBDataBase.user
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
        mockEngine=mockEngine,
    )


@pytest.fixture(scope="function")
def mockScheduleCRUD(mockSession, mockEngine):
    db = EBDataBase.schedule
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
        mockEngine=mockEngine,
    )


@pytest.fixture(scope="function")
def mockPathCRUD(mockSession, mockEngine):
    db = EBDataBase.path
    yield from getMockCRUD(
        mockSession=mockSession,
        db=db,
        mockEngine=mockEngine,
    )


@pytest.fixture(scope="function")
def mockUser(
    mockUserCRUD,
    mockEngine,
):
    dropTable(engine=mockEngine)
    mockUserCRUD.create(user=my_mock_user)
    yield my_mock_user
