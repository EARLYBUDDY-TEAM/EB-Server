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
def schedule_MockScheduleCRUD(mockScheduleCRUD):
    yield mockScheduleCRUD


@pytest.fixture(scope="function")
def schedule_MockUserCRUD(mockUserCRUD):
    yield mockUserCRUD


@pytest.fixture(scope="function")
def testClient(schedule_MockScheduleCRUD):
    def get_schedule_MockScheduleCRUD():
        yield schedule_MockScheduleCRUD

    app.dependency_overrides[EBDataBase.schedule.createCRUD] = (
        get_schedule_MockScheduleCRUD
    )
    testClient = TestClient(app)

    yield testClient

    del app.dependency_overrides[EBDataBase.schedule.createCRUD]
