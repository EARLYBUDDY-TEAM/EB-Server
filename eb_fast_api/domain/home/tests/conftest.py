import pytest
from eb_fast_api.database.tests.conftest import (
    mockScheduleCRUD,
    mockUserCRUD,
    mockPlaceCRUD,
    mockSession,
    mockPathCRUD,
    mockEngine,
    prepareTestDataBase,
    mockUser,
)


@pytest.fixture(scope="function")
def home_MockUser(mockUser):
    yield mockUser


@pytest.fixture(scope="function")
def home_MockSession(mockSession):
    yield mockSession


@pytest.fixture(scope="function")
def home_MockPathCRUD(mockPathCRUD):
    yield mockPathCRUD


@pytest.fixture(scope="function")
def home_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def home_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def home_MockPlaceCRUD(mockPlaceCRUD):
    yield mockPlaceCRUD


@pytest.fixture(scope="function")
def home_MockPathCRUD(mockPathCRUD):
    yield mockPathCRUD
