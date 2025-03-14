import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.service.jwt.sources.jwt_service import JWTService
from eb_fast_api.service.jwt.sources.jwt_service import getJWTService
from eb_fast_api.database.tests.conftest import (
    prepareTestDataBase,
    mockSession,
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
    mockEngine,
)
from eb_fast_api.database.sources.crud.cruds import UserCRUD


@pytest.fixture(scope="function")
def tokenMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def tokenMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def tokenmockPathCRUD(mockPathCRUD):
    yield mockPathCRUD


@pytest.fixture(scope="function")
def mockTestClient(
    tokenMockUserCRUD,
):
    app.dependency_overrides[UserCRUD] = tokenMockUserCRUD

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[UserCRUD]
    del testClient


@pytest.fixture(scope="function")
def realJWTService():
    service = JWTService()
    print("Create RealJWTService")

    yield service

    del service
    print("Del RealJWTService")
