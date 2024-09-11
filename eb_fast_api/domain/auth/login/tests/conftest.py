import pytest
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.tests.conftest import mockSession, mockUserCRUD
from typing import Annotated


@pytest.fixture(scope="function")
def loginMockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def testClient(loginMockUserCRUD):
    def getMockUserCRUD():
        yield loginMockUserCRUD

    # app.dependency_overrides[EBDatabase.user.depends()] = getMockUserCRUD
    app.dependency_overrides[EBDataBase.user.getCRUD] = getMockUserCRUD
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.user.depends()]
