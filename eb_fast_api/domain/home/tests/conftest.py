import pytest
from eb_fast_api.database.tests.conftest import (
    mockScheduleCRUD,
    mockUserCRUD,
    mockPlaceCRUD,
    mockSession,
    prepareTestDataBase,
)

@pytest.fixture(scope="function")
def home_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def home_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def home_MockPlaceCRUD(mockPlaceCRUD):
    yield mockPlaceCRUD
