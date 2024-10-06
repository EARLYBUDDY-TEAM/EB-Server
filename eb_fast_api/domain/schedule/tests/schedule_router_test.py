from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo, RegisterInfo
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import (
    mockGetUserEmail,
    mockEmail,
)


def test_addSchedule_SUCCESS(
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
):
    # given
    email = mockEmail
    password = "password"
    refreshToken = "refreshToken"
    nickName = "nickName"
    registerInfo = RegisterInfo(
        nickName=nickName,
        email=email,
        password=password,
    )
    user = registerInfo.toUser(refreshToken=refreshToken)
    schedule_MockUserCRUD.create(user)
    scheduleInfo = ScheduleInfo.mock()

    def getMockScheduleDB():
        yield schedule_MockScheduleCRUD

    app.dependency_overrides[EBDataBase.schedule.getCRUD] = getMockScheduleDB
    app.dependency_overrides[getUserEmail] = mockGetUserEmail

    testClient = TestClient(app)

    # when
    headers = {"access_token": "access_token"}
    json = scheduleInfo.model_dump(mode="json")
    response = testClient.post(
        "/schedule/add",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 200

    # restore dependencies
    del app.dependency_overrides[EBDataBase.schedule.getCRUD]
    del app.dependency_overrides[getUserEmail]

    # delete schedule table
    schedule_MockScheduleCRUD.dropTable(userEmail=email)


def test_addSchedule_FAIL(testClient):
    # given
    email = "email"
    scheduleInfo = ScheduleInfo.mock()
    json = scheduleInfo.model_dump(mode="json")
    headers = {"access_token": "access_token"}

    # when
    response = testClient.post("/schedule/add", headers=headers, json=json)

    # then
    assert response.status_code == 400
