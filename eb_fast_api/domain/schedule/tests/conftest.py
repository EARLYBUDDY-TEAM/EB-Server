import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.tests.conftest import (
    mockSession,
    mockScheduleCRUD,
    mockUserCRUD,
    mockPlaceCRUD,
    prepareTestDataBase,
    mockPathCRUD,
)
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.database.sources.database import EBDataBase


@pytest.fixture(scope="function")
def schedule_MockSession(mockSession):
    yield mockSession


@pytest.fixture(scope="function")
def schedule_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def schedule_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def schedule_MockPlaceCRUD(mockPlaceCRUD):
    yield mockPlaceCRUD


@pytest.fixture(scope="function")
def schedule_MockPathCRUD(mockPathCRUD):
    yield mockPathCRUD


@pytest.fixture(scope="session")
def testClient():
    def mock_def_session():
        yield mockSession

    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    app.dependency_overrides[EBDataBase.get_session] = mock_def_session
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[getUserEmail]
    del app.dependency_overrides[EBDataBase.get_session]
