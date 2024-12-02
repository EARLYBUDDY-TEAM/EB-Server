from eb_fast_api.service.notification.sources.feature.send_schedule_notification import (
    get_fcm_token,
    send_schedule_notification,
)
from unittest.mock import patch
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.testings import mock_notification_service as mns
from eb_fast_api.service.notification.testings import mock_notification_provider as mnp


def test_get_fcm_token():
    # given
    expected_fcm_token = "expected_fcm_token"
    mock_user_dict = {"fcm_token": expected_fcm_token}

    # when, then
    with patch.object(
        UserCRUD,
        "read",
        return_value=mock_user_dict,
    ):
        user_crud = EBDataBase.user.createCRUD()
        fcm_token = get_fcm_token(
            user_email="",
            user_crud=user_crud,
        )

        assert fcm_token == expected_fcm_token


def test_send_schedule_notification():
    # given
    patcher_get_fcm_token = mns.patcher_get_fcm_token(return_value="")
    patcher_send_notification = mns.patcher_send_notification()

    mock_noti_schedule = NotificationSchedule.mock()
    mock_provider = NotificationScheduleProvider()
    mock_provider.add_schedule(mock_noti_schedule)
    patcher_get_schedule = mnp.patcher_get_schedule()

    patcher_get_fcm_token.start()
    patcher_send_notification.start()
    patcher_get_schedule.start()

    assert len(mock_provider.data) == 1

    # when
    send_schedule_notification(provider=mock_provider)

    # then
    assert len(mock_provider.data) == 0

    patcher_get_fcm_token.stop()
    patcher_send_notification.stop()
    patcher_get_schedule.stop()
