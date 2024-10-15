from typing import List
from unittest.mock import patch
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.domain.home.sources.home_schema import ScheduleInfoList
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.home.testings.mock_home_feature import (
    mock_read_all_schedule,
    mock_schedule_dict_to_schedule_info,
    mockScheduleList,
    mockScheduleInfo,
)


def test_get_all_schedules():
    # given
    mock_read_all_schedule()
    mock_schedule_dict_to_schedule_info()
    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    testClient = TestClient(app)
    headers = {"access_token": "access_token"}

    # when
    response = testClient.get(
        "/home/get_all_schedules",
        headers=headers,
    )

    # then
    all_schedules: List[ScheduleInfo] = [
        mockScheduleInfo for _ in range(len(mockScheduleList))
    ]
    scheduleInfoList = ScheduleInfoList(all_schedules=all_schedules)
    expectModel = scheduleInfoList.model_dump(mode="json")
    responseModel = response.json()
    assert responseModel == expectModel


def test_delete_schedule_card_SUCCESS():
    def mock_delete_success(
        self,
        userEmail: str,
        scheduleID: int,
    ):
        return

    with patch(
        "eb_fast_api.database.sources.crud.schedule_crud.ScheduleCRUD.delete",
        mock_delete_success,
    ):
        app.dependency_overrides[getUserEmail] = mockGetUserEmail
        testClient = TestClient(app)
        headers = {"access_token": "access_token"}
        params = {"scheduleID": 10}

        # when
        response = testClient.delete(
            "/home/delete_schedule",
            params=params,
            headers=headers,
        )

        # then
        assert response.status_code == 200


def test_delete_schedule_card_FAIL():
    def mock_delete_fail(
        self,
        userEmail: str,
        scheduleID: int,
    ):
        raise Exception("mock_delete_fail")

    with patch(
        "eb_fast_api.database.sources.crud.schedule_crud.ScheduleCRUD.delete",
        mock_delete_fail,
    ):
        app.dependency_overrides[getUserEmail] = mockGetUserEmail
        testClient = TestClient(app)
        headers = {"access_token": "access_token"}
        params = {"scheduleID": 10}

        # when
        response = testClient.delete(
            "/home/delete_schedule",
            params=params,
            headers=headers,
        )

        # then
        assert response.status_code == 400
