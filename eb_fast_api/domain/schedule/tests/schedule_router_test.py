from eb_fast_api.main import app
from unittest.mock import patch
from fastapi.testclient import TestClient

from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.schedule.testings.mock_schedule_feature import (
    mock_create_schedule_SUCCESS,
    mock_create_schedule_FAIL,
    mock_update_schedule_SUCCESS,
    mock_update_schedule_FAIL,
)


def test_create_schedule_SUCCESS(testClient):
    # given
    mock_create_schedule_SUCCESS()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    schedule_info_json = scheduleInfo.model_dump(mode="json")
    json = {
        "scheduleInfo": schedule_info_json,
        "pathInfo": None,
    }

    # when
    response = testClient.post(
        "/schedule/create",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 200


def test_creaet_schedule_FAIL(testClient):
    # given
    mock_create_schedule_FAIL()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    schedule_info_json = scheduleInfo.model_dump(mode="json")
    json = {
        "scheduleInfo": schedule_info_json,
        "pathInfo": None,
    }

    # when
    response = testClient.post(
        "/schedule/create",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 400


def test_update_schedule_SUCCESS(testClient):
    # given
    mock_update_schedule_SUCCESS()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    schedule_info_json = scheduleInfo.model_dump(mode="json")
    json = {
        "scheduleInfo": schedule_info_json,
        "pathInfo": None,
    }

    # when
    response = testClient.patch(
        "/schedule/update",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 200


def test_update_schedule_FAIL(testClient):
    # given
    mock_update_schedule_FAIL()
    headers = {"access_token": "access_token"}
    scheduleInfo = ScheduleInfo.mock()
    schedule_info_json = scheduleInfo.model_dump(mode="json")
    json = {
        "scheduleInfo": schedule_info_json,
        "pathInfo": None,
    }

    # when
    response = testClient.patch(
        "/schedule/update",
        headers=headers,
        json=json,
    )

    # then
    assert response.status_code == 400


def test_delete_schedule_SUCCESS():
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
        params = {"schedule_id": "schedule_id"}

        # when
        response = testClient.delete(
            "/schedule/delete",
            params=params,
            headers=headers,
        )

        # then
        assert response.status_code == 200


def test_delete_schedule_FAIL():
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
        params = {"schedule_id": "schedule_id"}

        # when
        response = testClient.delete(
            "/schedule/delete",
            params=params,
            headers=headers,
        )

        # then
        assert response.status_code == 400
