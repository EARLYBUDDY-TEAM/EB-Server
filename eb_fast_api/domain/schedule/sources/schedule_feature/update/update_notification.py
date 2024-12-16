from eb_fast_api.domain.schedule.sources.schedule_feature.create.create_notification import (
    create_notification_schedule,
    create_notification_transport,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.delete.delete_notification import (
    delete_notification_schedule,
    delete_notification_transport,
)
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from datetime import datetime
from typing import Optional


def update_notification_schedule(
    user_email: str,
    schedule_info: ScheduleInfo,
    noti_schedule_provider: NotificationScheduleProvider,
    now: datetime,
):
    delete_notification_schedule(
        schedule_id=schedule_info.id,
        noti_schedule_provider=noti_schedule_provider,
    )
    create_notification_schedule(
        user_email=user_email,
        schedule_info=schedule_info,
        noti_schedule_provider=noti_schedule_provider,
        now=now,
    )


def update_notification_transport(
    user_email: str,
    schedule_info: ScheduleInfo,
    path_info: Optional[PathInfo],
    noti_transport_provider: NotificationTransportProvider,
    now: datetime,
):
    delete_notification_transport(
        schedule_id=schedule_info.id,
        noti_transport_provider=noti_transport_provider,
    )
    create_notification_transport(
        user_email=user_email,
        schedule_info=schedule_info,
        path_info=path_info,
        noti_transport_provider=noti_transport_provider,
        now=now,
    )
