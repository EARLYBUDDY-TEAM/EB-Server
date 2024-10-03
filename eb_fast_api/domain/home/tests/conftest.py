import pytest
from eb_fast_api.database.tests.conftest import (
    mockScheduleCRUD,
    mockUserCRUD,
    mockPlaceCRUD,
)
from eb_fast_api.domain.home.testings.mock_home_feature import mocking_home_feature


@pytest.fixture(scope="session")
def mock_home_feature():
    print("mock_home_feature, session start")
    mocking_home_feature()
    yield
    print("mock_home_feature, session finish")


@pytest.fixture(scope="function")
def home_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def home_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def home_MockPlaceCRUD(mockPlaceCRUD):
    yield mockPlaceCRUD
