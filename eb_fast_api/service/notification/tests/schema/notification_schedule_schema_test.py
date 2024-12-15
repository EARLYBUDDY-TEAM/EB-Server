from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from datetime import timedelta
from eb_fast_api.snippets.sources import eb_datetime


def test_cal_noti_time():
    # given
    now = eb_datetime.get_datetime_now()

    # when
    noti_time = NotificationSchedule.cal_noti_time(
        schedule_time=now,
        notify_schedule=0,
    )

    # then
    expected_noti_time = eb_datetime.get_only_time(now)
    assert noti_time == expected_noti_time


def test_cal_noti_time_return_None():
    # given
    now = eb_datetime.get_datetime_now() - timedelta(minutes=1)

    # when
    noti_time = NotificationSchedule.cal_noti_time(
        schedule_time=now,
        notify_schedule=0,
    )

    # then
    assert noti_time == None
