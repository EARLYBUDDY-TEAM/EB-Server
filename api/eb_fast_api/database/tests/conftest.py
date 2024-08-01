import pytest
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from eb_fast_api.database.sources.models import Base
from eb_fast_api.database.sources.crud import CRUD


@pytest.fixture(scope='session')
def mockEngine():
    filePath = str(Path(__file__).parent.absolute()) + "/mockdatabase.db"
    DB_URL = "sqlite:///" + filePath
    engine = create_engine(DB_URL)
    Base.metadata.create_all(bind=engine)

    yield engine

    engine.dispose()


@pytest.fixture(scope='session')
def makeMockSession(mockEngine):
    return scoped_session(sessionmaker(bind=mockEngine))


@pytest.fixture(scope='session')
def makeMockCRUD(makeMockSession):
    with CRUD(session = makeMockSession) as crud:
        yield crud


@pytest.fixture(scope='function')
def mockCRUD(makeMockCRUD):
    yield makeMockCRUD
    makeMockCRUD.rollback()