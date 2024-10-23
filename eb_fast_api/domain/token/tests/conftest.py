import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.service.jwt.sources.jwt_service import JWTService
from eb_fast_api.service.jwt.tests.conftest import mockJWTService
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.database.tests.conftest import (
    prepareTestDataBase,
    mockSession,
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
)


@pytest.fixture(scope="function")
def tokenMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def tokenMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD

@pytest.fixture(scope="function")
def tokenMockRouteCRUD(mockRouteCRUD):
    yield mockRouteCRUD


@pytest.fixture(scope="function")
def tokenMockJWTService(mockJWTService):
    yield mockJWTService


@pytest.fixture(scope="function")
def mockTestClient(tokenMockJWTService):
    def getMockJWTService():
        yield tokenMockJWTService

    app.dependency_overrides[getJWTService] = getMockJWTService

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[getJWTService]
    del testClient


@pytest.fixture(scope="function")
def realJWTService():
    service = JWTService()
    print("Create RealJWTService")

    yield service

    del service
    print("Del RealJWTService")
