from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
)
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PathCRUD
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    bisect_schedule as bs,
)
from datetime import datetime
from typing import Optional


def add_notification_schedule_to_provider(
    user_email: str,
    schedule_id: str,
    schedule_title: str,
    notify_schedule: int,
    schedule_time: datetime,
    noti_schedule_provider: NotificationScheduleProvider,
    now: datetime,
) -> bool:
    noti_schedule = NotificationSchedule.init(
        user_email=user_email,
        schedule_id=schedule_id,
        schedule_title=schedule_title,
        notify_schedule=notify_schedule,
        schedule_time=schedule_time,
        now=now,
    )

    if noti_schedule == None:
        return False

    add_result = noti_schedule_provider.add_notification(
        noti_schema=noti_schedule,
        now=now,
    )
    return add_result


def add_notification_transport_to_provider(
    user_email: str,
    schedule_id: str,
    schedule_name: str,
    schedule_time: datetime,
    notify_transport: int,
    notify_transport_range: int,
    path_dict: dict,
    noti_transport_provider: NotificationTransportProvider,
    now: datetime,
) -> bool:
    noti_schedule = NotificationTransport.init(
        user_email=user_email,
        schedule_id=schedule_id,
        schedule_name=schedule_name,
        schedule_time=schedule_time,
        notify_transport=notify_transport,
        notify_transport_range=notify_transport_range,
        path_dict=path_dict,
        now=now,
    )

    if noti_schedule == None:
        return False

    add_result = noti_transport_provider.add_notification(
        noti_schema=noti_schedule,
        now=now,
    )
    return add_result


def prepare_add_noti_transport_to_provider(
    notify_transport: Optional[int],
    notify_transport_range: Optional[int],
    path_dict: Optional[dict],
) -> bool:
    return (
        notify_transport is not None
        and notify_transport_range is not None
        and path_dict is not None
    )


def prepare_add_noti_schedule_to_provider(
    notify_schedule: Optional[int],
) -> bool:
    return notify_schedule is not None


def add_notification_to_provider(
    user_email: str,
    schedule_crud: ScheduleCRUD,
    path_crud: PathCRUD,
    noti_schedule_provider: NotificationScheduleProvider,
    noti_transport_provider: NotificationTransportProvider,
):
    schedule_dict_list = schedule_crud.read_all(userEmail=user_email)
    if not schedule_dict_list:
        return

    now = eb_datetime.get_datetime_now()
    now_date = now.date()
    left = bs.get_left_index(
        schedule_dict_list=schedule_dict_list,
        today_date=now_date,
    )
    right = bs.get_right_index(
        schedule_dict_list=schedule_dict_list,
        today_date=now_date,
    )

    if schedule_dict_list[left]["time"].date() != now_date:
        return

    schedule_noti_count = 0
    transport_noti_count = 0
    for i in range(left, right):
        schedule_dict = schedule_dict_list[i]
        schedule_id = schedule_dict["id"]
        schedule_title = schedule_dict["title"]
        notify_schedule = schedule_dict["notify_schedule"]
        schedule_time = schedule_dict["time"]

        if prepare_add_noti_schedule_to_provider(notify_schedule=notify_schedule):
            if add_notification_schedule_to_provider(
                user_email=user_email,
                schedule_id=schedule_id,
                schedule_title=schedule_title,
                notify_schedule=notify_schedule,
                schedule_time=schedule_time,
                noti_schedule_provider=noti_schedule_provider,
                now=now,
            ):
                schedule_noti_count += 1

        notify_transport = schedule_dict["notify_transport"]
        notify_transport_range = schedule_dict["notify_transport_range"]
        path_dict = path_crud.read(
            user_email=user_email,
            path_id=schedule_id,
        )
        if prepare_add_noti_transport_to_provider(
            notify_transport=notify_transport,
            notify_transport_range=notify_transport_range,
            path_dict=path_dict,
        ):
            if add_notification_transport_to_provider(
                user_email=user_email,
                schedule_dict=schedule_dict,
                noti_transport_provider=noti_transport_provider,
                path_crud=path_crud,
                now=now,
            ):
                transport_noti_count += 1
    else:
        logger.debug(f"user_email : {user_email}")
        logger.debug(f"add_today_schedule_notification count : {schedule_noti_count}")
        logger.debug(f"add_today_transport_notification count : {transport_noti_count}")
