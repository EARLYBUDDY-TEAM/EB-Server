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


@pytest.fixture(scope="function")
def registerMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def registerMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def testClient(registerMockUserCRUD):
    def getMockUserCRUD():
        yield registerMockUserCRUD

    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD

    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.user.getCRUD]
