from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
import heapq
from eb_fast_api.snippets.sources import eb_datetime
from datetime import timedelta


def test_notification_schedule_provider_add_delete():
    # given
    noti_schedule_provider = NotificationScheduleProvider()
    noti_schedule = NotificationSchedule.mock()

    # when, then
    noti_schedule_provider.add_schedule(noti_schedule=noti_schedule)
    assert noti_schedule_provider.data[0] == noti_schedule

    noti_schedule_provider.delete_schedule(id=noti_schedule.id)
    assert len(noti_schedule_provider.data) == 0


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
        noti_schedule_provider.add_schedule(noti_schedule=noti_schedule)

    # when
    noti_schedule_list = noti_schedule_provider.get_schedule(now=now)

    # then
    assert len(noti_schedule_list) == 1
    assert noti_schedule_list[0] == noti_schedule1
