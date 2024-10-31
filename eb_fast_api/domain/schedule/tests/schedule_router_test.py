from eb_fast_api.main import app
from fastapi.testclient import TestClient

from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.schedule.testings.mock_schedule_feature import (
    mock_create_schedule_SUCCESS,
    mock_create_schedule_FAIL,
    mock_update_schedule_SUCCESS,
    mock_update_schedule_FAIL,
    mock_delete_schedule_SUCCESS,
    mock_delete_schedule_FAIL,
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


def test_delete_schedule_SUCCESS(
    schedule_MockSession,
):
    mock_delete_schedule_SUCCESS()

    def mock_def_session():
        yield schedule_MockSession

    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    app.dependency_overrides[EBDataBase.get_session] = mock_def_session
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


def test_delete_schedule_card_FAIL(
    schedule_MockSession,
):
    mock_delete_schedule_FAIL()

    def mock_def_session():
        yield schedule_MockSession

    app.dependency_overrides[getUserEmail] = mockGetUserEmail
    app.dependency_overrides[EBDataBase.get_session] = mock_def_session
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
