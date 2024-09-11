import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.tests.conftest import (
    mockSession,
    mockScheduleCRUD,
    mockUserCRUD,
)


@pytest.fixture(scope="function")
def scheduleMockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def scheduleMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def testClient(scheduleMockDB):
    def getMockDB():
        yield scheduleMockDB

    app.dependency_overrides[EBDataBase.schedule.depends()] = scheduleMockScheduleCRUD
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.schedule.depends()]
