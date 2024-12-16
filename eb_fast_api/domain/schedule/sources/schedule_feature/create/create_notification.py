from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    add_notification_to_provider as antp,
)
from typing import Optional
from datetime import datetime


def create_notification_transport(
    user_email: str,
    schedule_info: ScheduleInfo,
    path_info: Optional[PathInfo],
    noti_transport_provider: NotificationTransportProvider,
    now: datetime,
) -> bool:
    notify_transport = schedule_info.notify_transport
    notify_transport_range = schedule_info.notify_transport_range
    if path_info is None:
        return False
    path_dict = path_info.model_dump(mode="json")

    if not antp.prepare_add_noti_transport_to_provider(
        notify_transport=notify_transport,
        notify_transport_range=notify_transport_range,
        path_dict=path_dict,
    ):
        return False

    add_result = antp.add_notification_transport_to_provider(
        user_email=user_email,
        schedule_id=schedule_info.id,
        schedule_name=schedule_info.title,
        schedule_time=schedule_info.time,
        notify_transport=notify_transport,
        notify_transport_range=notify_transport_range,
        path_dict=path_dict,
        noti_transport_provider=noti_transport_provider,
        now=now,
    )
    return add_result


def create_notification_schedule(
    user_email: str,
    schedule_info: ScheduleInfo,
    noti_schedule_provider: NotificationScheduleProvider,
    now: datetime,
) -> bool:
    notify_schedule = schedule_info.notify_schedule
    if not antp.prepare_add_noti_schedule_to_provider(
        notify_schedule=notify_schedule,
    ):
        return False

    add_result = antp.add_notification_schedule_to_provider(
        user_email=user_email,
        schedule_id=schedule_info.id,
        schedule_title=schedule_info.title,
        notify_schedule=notify_schedule,
        schedule_time=schedule_info.time,
        now=now,
        noti_schedule_provider=noti_schedule_provider,
    )

    return add_result
