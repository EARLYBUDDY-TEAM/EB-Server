from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_notification_schedule as cns,
)
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from uuid import uuid4
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.snippets.sources import eb_datetime
from datetime import timedelta


def test_create_notification_schedule():
    # given
    user_email = "test@test.com"
    notify_schedule = 0
    now = eb_datetime.get_datetime_now()
    schedule_info1 = ScheduleInfo.mock(id=str(uuid4()))
    schedule_info1.notify_schedule = notify_schedule
    schedule_info1.time = now

    schedule_info2 = ScheduleInfo.mock(id=str(uuid4()))
    schedule_info2.notify_schedule = notify_schedule
    schedule_info2.time = now - timedelta(days=1)

    noti_schedule_provider = NotificationScheduleProvider()
    expected_noti_schedule = NotificationSchedule.init(
        user_email=user_email,
        schedule_id=schedule_info1.id,
        schedule_title=schedule_info1.title,
        notify_schedule=schedule_info1.notify_schedule,
        schedule_time=schedule_info1.time,
        now=now,
    )

    # when
    cns.create_notification_schedule(
        user_email=user_email,
        schedule_info=schedule_info1,
        noti_schedule_provider=noti_schedule_provider,
    )
    cns.create_notification_schedule(
        user_email=user_email,
        schedule_info=schedule_info2,
        noti_schedule_provider=noti_schedule_provider,
    )

    # then
    noti_schedule = noti_schedule_provider.data[0]
    assert noti_schedule == expected_noti_schedule
    assert len(noti_schedule_provider.data) == 1
