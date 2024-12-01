from eb_fast_api.domain.schedule.sources.schedule_feature.create.create_notification_schedule import create_notification_schedule
from eb_fast_api.domain.schedule.sources.schedule_feature.delete.delete_notification_schedule import delete_notification_schedule
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo


def update_notification_schedule(
    user_email: str,
    schedule_info: ScheduleInfo,
    noti_schedule_provider: NotificationScheduleProvider,
):
    delete_notification_schedule(
        schedule_id=schedule_info.id,
        noti_schedule_provider=noti_schedule_provider,
    )
    create_notification_schedule(
        user_email=user_email,
        schedule_info=schedule_info,
        noti_schedule_provider=noti_schedule_provider,
    )
