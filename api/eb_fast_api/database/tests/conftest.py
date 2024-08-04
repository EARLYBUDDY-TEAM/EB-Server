import pytest
from eb_fast_api.database.testings.mock_crud import mockSessionMaker, MockCRUD


@pytest.fixture(scope='session')
def createDB():
    session = mockSessionMaker()
    crud = MockCRUD(session = session)
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