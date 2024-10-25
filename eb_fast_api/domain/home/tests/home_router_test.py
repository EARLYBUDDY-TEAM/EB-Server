from unittest.mock import patch
from fastapi.testclient import TestClient
from typing import List

from eb_fast_api.main import app
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.home.testings.mock_home_feature import (
    mock_read_all_schedule,
    mock_schedule_dict_to_schedule_path_info,
    mockScheduleList,
    mockSchedulePathInfo,
)
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.home.sources.home_schema import (
    SchedulePathInfo,
    SchedulePathInfoList,
)


def test_get_all_schedules(home_MockSession):
    def mock_def_session():
        yield home_MockSession

    # given
    mock_read_all_schedule()
    mock_schedule_dict_to_schedule_path_info()
    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    app.dependency_overrides[EBDataBase.get_session] = mock_def_session
    testClient = TestClient(app)
    headers = {"access_token": "access_token"}

    # when
    response = testClient.get(
        "/home/get_all_schedules",
        headers=headers,
    )

    # then
    all_schedules: List[SchedulePathInfo] = [
        mockSchedulePathInfo for _ in range(len(mockScheduleList))
    ]
    schedulePathInfoList = SchedulePathInfoList(all_schedules=all_schedules)
    assert response.json() == schedulePathInfoList.model_dump(mode="json")

    del app.dependency_overrides[getUserEmail]
    del app.dependency_overrides[EBDataBase.get_session]


def test_delete_schedule_card_SUCCESS():
    def mock_delete_success(
        self,
        userEmail: str,
        scheduleID: str,
    ):
        return

    with patch(
        "eb_fast_api.database.sources.crud.schedule_crud.ScheduleCRUD.delete",
        mock_delete_success,
    ):
        app.dependency_overrides[getUserEmail] = mockGetUserEmail
        testClient = TestClient(app)
        headers = {"access_token": "access_token"}
        params = {"scheduleID": "scheduleID"}

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
        scheduleID: str,
    ):
        raise Exception("mock_delete_fail")

    with patch(
        "eb_fast_api.database.sources.crud.schedule_crud.ScheduleCRUD.delete",
        mock_delete_fail,
    ):
        app.dependency_overrides[getUserEmail] = mockGetUserEmail
        testClient = TestClient(app)
        headers = {"access_token": "access_token"}
        params = {"scheduleID": "scheduleID"}

        # when
        response = testClient.delete(
            "/home/delete_schedule",
            params=params,
            headers=headers,
        )

        # then
        assert response.status_code == 400
