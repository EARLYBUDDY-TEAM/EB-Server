import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.database.tests.conftest import createDB, mockDB


@pytest.fixture(scope="function")
def loginMockDB(mockDB):
    yield mockDB


@pytest.fixture(scope="function")
def testClient(loginMockDB):
    def getMockDB():
        yield loginMockDB

    app.dependency_overrides[getDB] = getMockDB
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[getDB]
