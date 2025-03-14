import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.tests.conftest import (
    prepareTestDataBase,
    mockSession,
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
    mockEngine,
    mockDefCreateEngine,
)
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.service.jwt.tests.conftest import mockJWTService
from eb_fast_api.domain.token.eb_token.testings.mock_eb_token_feature import (
    mockGetUserEmail,
)
from eb_fast_api.domain.token.eb_token.sources.eb_token_feature import getUserEmail


@pytest.fixture(scope="function")
def authMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def authMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def authMockPathCRUD(mockPathCRUD):
    yield mockPathCRUD


@pytest.fixture(scope="function")
def authMockJWTService(mockJWTService):
    yield mockJWTService


@pytest.fixture(scope="function")
def authMockSession(mockSession):
    yield mockSession


@pytest.fixture(scope="function")
def authMockDefCreateEngine(mockDefCreateEngine):
    yield mockDefCreateEngine


@pytest.fixture(scope="function")
def testClient(authMockUserCRUD, authMockJWTService, authMockDefCreateEngine):
    def getMockUserCRUD():
        yield authMockUserCRUD

    def getMockJWTService():
        yield authMockJWTService

    def getMockDefCreateEngine():
        yield authMockDefCreateEngine

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    app.dependency_overrides[EBDataBase.get_def_create_engine] = getMockDefCreateEngine
    app.dependency_overrides[getJWTService] = getMockJWTService
    app.dependency_overrides[getUserEmail] = mockGetUserEmail

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.user.getCRUD]
    del app.dependency_overrides[EBDataBase.get_def_create_engine]
    del app.dependency_overrides[getJWTService]
    del app.dependency_overrides[getUserEmail]
    del testClient
