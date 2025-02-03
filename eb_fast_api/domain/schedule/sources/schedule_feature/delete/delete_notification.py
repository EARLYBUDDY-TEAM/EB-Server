from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.snippets.sources.logger import logger


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
    logger.debug("--------------------------------")
    logger.debug("delete_notification_transport")
    logger.debug(f"schedule_id : {schedule_id}")
    logger.debug("--------------------------------")
    noti_transport_provider.delete_notification(
        schedule_id=schedule_id,
    )
