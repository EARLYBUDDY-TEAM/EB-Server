from eb_fast_api.service.notification.sources.feature.schedule.send_schedule_notification import (
    send_schedule_notification,
)
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.testings import (
    mock_fcm_feature as mff,
)
from eb_fast_api.service.notification.testings import (
    mock_notification_schedule_provider as mnsp,
)
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.snippets.testings import mock_eb_datetime as med
from datetime import datetime


def test_send_schedule_notification():
    # given
    now = eb_datetime.get_datetime_now()
    patcher_get_datetime_now = med.patcher_get_datetime_now(return_value=now)
    patcher_get_fcm_token = mff.patcher_get_fcm_token(return_value="")
    patcher_send_notification = mff.patcher_send_notification()

    mock_noti_schedule = NotificationSchedule.mock(schedule_time=now)
    mock_provider = NotificationScheduleProvider()
    mock_provider.add_notification(
        noti_schema=mock_noti_schedule,
        now=now,
    )
    patcher_get_notification = mnsp.patcher_get_notification()

    patcher_get_fcm_token.start()
    patcher_send_notification.start()
    patcher_get_notification.start()
    patcher_get_datetime_now.start()

    assert len(mock_provider.data) == 1

    # when
    send_schedule_notification(
        provider=mock_provider,
    )

    # then
    assert len(mock_provider.data) == 0

    patcher_get_fcm_token.stop()
    patcher_send_notification.stop()
    patcher_get_notification.stop()
    patcher_get_datetime_now.stop()
