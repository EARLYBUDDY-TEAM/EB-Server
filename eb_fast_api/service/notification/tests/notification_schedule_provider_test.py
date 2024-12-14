from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.snippets.testings import mock_eb_datetime as med
from datetime import timedelta


def test_notification_schedule_provider_add_delete():
    # given
    now = eb_datetime.get_datetime_now()
    patcher = med.patcher_get_datetime_now(now)
    patcher.start()

    noti_schedule_provider = NotificationScheduleProvider()
    noti_schedule = NotificationSchedule.mock(schedule_time=now)

    # when, then
    noti_schedule_provider.add_notification(noti_schedule=noti_schedule, now=now)
    assert noti_schedule_provider.data[0] == noti_schedule

    noti_schedule_provider.delete_notification(schedule_id=noti_schedule.schedule_id)
    assert len(noti_schedule_provider.data) == 0

    patcher.stop()


def test_notification_schedule_provider_get_schedule():
    now = eb_datetime.get_datetime_now()

    # given
    noti_schedule1 = NotificationSchedule.mock(schedule_time=now)
    noti_schedule2 = NotificationSchedule.mock(
        schedule_time=now + timedelta(minutes=10)
    )
    noti_schedule3 = NotificationSchedule.mock(
        schedule_time=now + timedelta(minutes=20)
    )
    noti_schedule_list = [
        noti_schedule1,
        noti_schedule2,
        noti_schedule3,
    ]
    noti_schedule_provider = NotificationScheduleProvider()
    for noti_schedule in noti_schedule_list:
        noti_schedule_provider.add_notification(noti_schedule=noti_schedule, now=now)

    # when
    noti_schedule_list = noti_schedule_provider.get_notification(now=now)

    # then
    assert len(noti_schedule_list) == 1
    assert noti_schedule_list[0] == noti_schedule1
