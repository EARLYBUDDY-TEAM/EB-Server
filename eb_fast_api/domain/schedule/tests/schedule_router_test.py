from eb_fast_api.domain.schedule.sources.schedule_schema import AddScheduleInfo
from eb_fast_api.domain.schedule.testings.mock_schedule_feature import (
    mock_create_schedule_SUCCESS,
    mock_create_schedule_FAIL,
)
from unittest.mock import patch


def test_addSchedule_SUCCESS(testClient):
    # given
    with patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.createSchedule",
        mock_create_schedule_SUCCESS,
    ):
        headers = {"access_token": "access_token"}
        addScheduleInfo = AddScheduleInfo.mock()
        json = addScheduleInfo.model_dump(mode="json")

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
    with patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.createSchedule",
        mock_create_schedule_FAIL,
    ):
        headers = {"access_token": "access_token"}
        addScheduleInfo = AddScheduleInfo.mock()
        json = addScheduleInfo.model_dump(mode="json")

        # when
        response = testClient.post(
            "/schedule/add",
            headers=headers,
            json=json,
        )

        # then
        assert response.status_code == 400
