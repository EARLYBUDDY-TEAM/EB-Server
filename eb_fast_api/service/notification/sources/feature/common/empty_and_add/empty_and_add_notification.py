from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
    noti_schedule_provider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
    noti_transport_provider,
)
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
)
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, UserCRUD, PathCRUD
from typing import List
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    bisect_schedule as bs,
)
from datetime import datetime


def add_notification_schedule_to_provider(
    user_email: str,
    schedule_dict: dict,
    noti_schedule_provider: NotificationScheduleProvider,
    now: datetime,
) -> bool:
    notify_schedule = schedule_dict["notify_schedule"]
    if notify_schedule == None:
        return False

    schedule_id = schedule_dict["id"]
    schedule_title = schedule_dict["title"]
    schedule_time = schedule_dict["time"]
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
    schedule_dict: dict,
    noti_transport_provider: NotificationTransportProvider,
    path_crud: PathCRUD,
    now: datetime,
) -> bool:
    notify_transport = schedule_dict["notify_transport"]
    notify_transport_range = schedule_dict["notify_transport_range"]

    if notify_transport is None or notify_transport_range is None:
        return False

    schedule_id = schedule_dict["id"]
    path_dict = path_crud.read(
        user_email=user_email,
        path_id=schedule_id,
    )
    if path_dict is None:
        return False

    schedule_name = schedule_dict["title"]
    schedule_time = schedule_dict["time"]

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

        if add_notification_schedule_to_provider(
            user_email=user_email,
            schedule_dict=schedule_dict,
            noti_schedule_provider=noti_schedule_provider,
            now=now,
        ):
            schedule_noti_count += 1

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


def get_all_user(
    user_crud: UserCRUD,
) -> List[dict]:
    return user_crud.read_all()


def empty_and_add_all_user_notification(
    noti_schedule_provider=noti_schedule_provider,
    noti_transport_provider=noti_transport_provider,
    session=EBDataBase.create_session(),
    engine=EBDataBase.create_engine(),
):
    user_crud = EBDataBase.user.createCRUD(
        session=session,
        engine=engine,
    )
    schedule_crud = EBDataBase.schedule.createCRUD(
        session=session,
        engine=engine,
    )
    path_crud = EBDataBase.path.createCRUD(
        session=session,
        engine=engine,
    )
    all_users = get_all_user(user_crud=user_crud)

    noti_schedule_provider.data = []
    noti_transport_provider.data = []

    for user in all_users:
        user_email = user["email"]
        add_notification_to_provider(
            user_email=user_email,
            schedule_crud=schedule_crud,
            path_crud=path_crud,
            noti_schedule_provider=noti_schedule_provider,
            noti_transport_provider=noti_transport_provider,
        )
