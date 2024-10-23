import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.tests.conftest import (
    prepareTestDataBase,
    mockSession,
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
)
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.service.jwt.tests.conftest import mockJWTService


@pytest.fixture(scope="function")
def loginMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def loginMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def loginMockRouteCRUD(mockRouteCRUD):
    yield mockRouteCRUD


@pytest.fixture(scope="function")
def loginMockJWTService(mockJWTService):
    yield mockJWTService


@pytest.fixture(scope="function")
def testClient(loginMockUserCRUD, loginMockJWTService):
    def getMockUserCRUD():
        yield loginMockUserCRUD

    def getMockJWTService():
        yield loginMockJWTService

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    app.dependency_overrides[getJWTService] = getMockJWTService

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.user.getCRUD]
    del app.dependency_overrides[getJWTService]
    del testClient
