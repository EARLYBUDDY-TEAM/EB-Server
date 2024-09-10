from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo, UserInfo


def test_addSchedule_SUCCESS(scheduleMockDB):
    # given
    email = "email"
    password = "password"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
    scheduleMockDB.userCreate(user)
    scheduleInfo = ScheduleInfo.mock()

    def getMockDB():
        yield scheduleMockDB

    app.dependency_overrides[getDB] = getMockDB
    testClient = TestClient(app)

    # when
    params = {"userEmail": email}
    json = scheduleInfo.model_dump(mode="json")
    response = testClient.post("/schedule/add", params=params, json=json)

    # then
    assert response.status_code == 200


def test_addSchedule_FAIL(testClient):
    # given, when
    email = "email"
    scheduleInfo = ScheduleInfo.mock()
    params = {"userEmail": email}
    json = scheduleInfo.model_dump(mode="json")
    response = testClient.post("/schedule/add", params=params, json=json)

    # then
    assert response.status_code == 400
