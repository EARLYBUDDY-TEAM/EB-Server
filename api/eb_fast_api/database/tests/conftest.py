import pytest
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from eb_fast_api.database.sources.models import Base


'''
처음, mockDB init

각 테스트 끝나면 db.rollback

파일 마지막 mockDB deinit
'''


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


@pytest.fixture(scope='function')
def mockSession(makeMockSession):
    session = makeMockSession()

    yield session

    session.rollback()
    session.close()