import pytest
from eb_fast_api.database.testings.mock_crud import mockSessionMaker
from eb_fast_api.database.sources.crud import CRUD


@pytest.fixture(scope='session')
def createDB():
    session = mockSessionMaker()
    crud = CRUD(session = session)
    print('create CRUD !!!')
    yield crud
    session.close()
    del crud
    print('deinit CRUD !!!')


@pytest.fixture(scope='function')
def mockDB(createDB):
    yield createDB
    createDB.rollback()
    print('rollback !!!')