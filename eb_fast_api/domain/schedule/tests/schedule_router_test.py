from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.domain.schedule.testings.mock_schedule_feature import (
    mock_create_schedule_SUCCESS,
    mock_create_schedule_FAIL,
)


def test_addSchedule_SUCCESS(testClient):
    # given
    mock_create_schedule_SUCCESS()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    json = scheduleInfo.model_dump(mode="json")

    # when
    response = testClient.post(
        "/schedule/add",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 200


def test_addSchedule_FAIL(testClient):
    # given
    mock_create_schedule_FAIL()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    json = scheduleInfo.model_dump(mode="json")

    # when
    response = testClient.post(
        "/schedule/add",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 400
