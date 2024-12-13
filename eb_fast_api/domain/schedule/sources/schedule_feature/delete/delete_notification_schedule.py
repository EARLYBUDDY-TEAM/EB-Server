from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)


def delete_notification_schedule(
    schedule_id: str,
    noti_schedule_provider: NotificationScheduleProvider,
):
    noti_schedule_provider.delete_schedule(
        id=schedule_id,
    )
