from eb_fast_api.main import app
from fastapi.testclient import TestClient

from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.schedule.testings import mock_schedule_feature as msf


def test_create_schedule_SUCCESS(testClient):
    # given
    patcher_create_schedule_SUCCESS = msf.patcher_create_schedule_SUCCESS()
    patcher_create_notification_schedule_SUCCESS = (
        msf.patcher_create_notification_schedule_SUCCESS()
    )
    patcher_create_schedule_SUCCESS.start()
    patcher_create_notification_schedule_SUCCESS.start()

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
    patcher_create_schedule_SUCCESS.stop()
    patcher_create_notification_schedule_SUCCESS.stop()


def test_create_schedule_FAIL_create_schedule(testClient):
    # given
    patcher_create_schedule_FAIL = msf.patcher_create_schedule_FAIL()
    patcher_create_schedule_FAIL.start()

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
    patcher_create_schedule_FAIL.stop()


def test_create_schedule_FAIL_create_notification_schedule(testClient):
    # given
    patcher_create_schedule_SUCCESS = msf.patcher_create_schedule_SUCCESS()
    patcher_create_notification_schedule_FAIL = (
        msf.patcher_create_notification_schedule_FAIL()
    )
    patcher_create_schedule_SUCCESS.start()
    patcher_create_notification_schedule_FAIL.start()

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
    assert response.status_code == 401
    patcher_create_schedule_SUCCESS.stop()
    patcher_create_notification_schedule_FAIL.stop()


def test_update_schedule_SUCCESS(testClient):
    # given
    patcher_update_schedule_SUCCESS = msf.patcher_update_schedule_SUCCESS()
    patcher_update_schedule_SUCCESS.start()

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
    patcher_update_schedule_SUCCESS.stop()


def test_update_schedule_FAIL(testClient):
    # given
    patcher_update_schedule_FAIL = msf.patcher_update_schedule_FAIL()
    patcher_update_schedule_FAIL.start()

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
    patcher_update_schedule_FAIL.stop()


def test_update_schedule_FAIL_update_notification_schedule(testClient):
    # given
    patcher_update_schedule_SUCCESS = msf.patcher_update_schedule_SUCCESS()
    patcher_update_notification_schedule_FAIL = (
        msf.patcher_update_notification_schedule_FAIL()
    )
    patcher_update_schedule_SUCCESS.start()
    patcher_update_notification_schedule_FAIL.start()

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
    assert response.status_code == 401
    patcher_update_schedule_SUCCESS.stop()
    patcher_update_notification_schedule_FAIL.stop()


def test_delete_schedule_SUCCESS(
    schedule_MockSession,
):
    patcher_delete_schedule_SUCCESS = msf.patcher_delete_schedule_SUCCESS()
    patcher_delete_schedule_SUCCESS.start()

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
    patcher_delete_schedule_SUCCESS.stop()


def test_delete_schedule_card_FAIL(
    schedule_MockSession,
):
    patcher_delete_schedule_FAIL = msf.patcher_delete_schedule_FAIL()
    patcher_delete_schedule_FAIL.start()

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
    patcher_delete_schedule_FAIL.stop()


def test_delete_schedule_card_FAIL_delete_notification_schedule(
    schedule_MockSession,
):
    patcher_delete_schedule_SUCCESS = msf.patcher_delete_schedule_SUCCESS()
    patcher_delete_notification_schedule_FAIL = (
        msf.patcher_delete_notification_schedule_FAIL()
    )
    patcher_delete_schedule_SUCCESS.start()
    patcher_delete_notification_schedule_FAIL.start()

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
    assert response.status_code == 401
    patcher_delete_schedule_SUCCESS.stop()
    patcher_delete_notification_schedule_FAIL.stop()
