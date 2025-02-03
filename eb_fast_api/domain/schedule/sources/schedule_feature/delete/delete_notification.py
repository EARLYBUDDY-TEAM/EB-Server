from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)


def delete_notification_schedule(
    schedule_id: str,
    noti_schedule_provider: NotificationScheduleProvider,
):
    noti_schedule_provider.delete_notification(
        schedule_id=schedule_id,
    )


def delete_notification_transport(
    schedule_id: str,
    noti_transport_provider: NotificationTransportProvider,
):
    noti_transport_provider.delete_notification(
        schedule_id=schedule_id,
    )
