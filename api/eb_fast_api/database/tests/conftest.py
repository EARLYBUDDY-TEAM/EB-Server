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
def db_engine():
    filePath = str(Path(__file__).parent.absolute()) + "/mockdatabase.db"
    DB_URL = "sqlite:///" + filePath
    engine = create_engine(DB_URL)
    Base.metadata.create_all(bind=engine)

    yield engine

    engine.dispose()


@pytest.fixture(scope='session')
def db_session_factory(db_engine):
    return scoped_session(sessionmaker(bind=db_engine))


@pytest.fixture(scope='function')
def mock_db(db_session_factory):
    session = db_session_factory()

    yield session

    print('rollback???')
    session.rollback()
    session.close()