import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.tests.conftest import (
    mockSession,
    mockScheduleCRUD,
    mockUserCRUD,
    mockPlaceCRUD,
    prepareTestDataBase,
)
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail


@pytest.fixture(scope="function")
def schedule_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def schedule_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def schedule_MockPlaceCRUD(mockPlaceCRUD):
    yield mockPlaceCRUD


@pytest.fixture(scope="session")
def testClient():
    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[getUserEmail]
