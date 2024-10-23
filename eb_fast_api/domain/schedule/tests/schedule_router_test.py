from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.domain.schedule.testings.mock_schedule_feature import (
    mock_create_schedule_SUCCESS,
    mock_create_schedule_FAIL,
    mock_update_schedule_with_info_SUCCESS,
    mock_update_schedule_with_info_FAIL,
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


def test_update_schedule_SUCCESS(testClient):
    # given
    mock_update_schedule_with_info_SUCCESS()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    json = scheduleInfo.model_dump(mode="json")

    # when
    response = testClient.post(
        "/schedule/update",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 200


def test_update_schedule_FAIL(testClient):
    # given
    mock_update_schedule_with_info_FAIL()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    json = scheduleInfo.model_dump(mode="json")

    # when
    response = testClient.post(
        "/schedule/update",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 400
