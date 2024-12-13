from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)


def create_notification_schedule(
    user_email: str,
    schedule_info: ScheduleInfo,
    noti_schedule_provider: NotificationScheduleProvider,
):
    notify_schedule = schedule_info.notify_schedule
    if notify_schedule == None:
        return

    noti_schedule = NotificationSchedule.init(
        user_email=user_email,
        schedule_id=schedule_info.id,
        schedule_title=schedule_info.title,
        notify_schedule=notify_schedule,
        schedule_time=schedule_info.time,
    )

    if noti_schedule == None:
        return

    noti_schedule_provider.add_schedule(
        noti_schedule=noti_schedule,
    )
