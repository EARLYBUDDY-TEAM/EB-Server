import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.tests.conftest import (
    mockSession,
    mockUserCRUD,
    prepareTestDataBase,
    mockScheduleCRUD,
)
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.service.jwt.tests.conftest import mockJWTService


@pytest.fixture(scope="function")
def registerMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def registerMockJWTService(mockJWTService):
    yield mockJWTService


@pytest.fixture(scope="function")
def registerMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def testClient(registerMockUserCRUD, registerMockJWTService):
    def getMockUserCRUD():
        yield registerMockUserCRUD

    def getMockJWTService():
        yield registerMockJWTService

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    app.dependency_overrides[getJWTService] = getMockJWTService

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.user.getCRUD]
    del app.dependency_overrides[getJWTService]
