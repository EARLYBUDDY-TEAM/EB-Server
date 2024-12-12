from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
    noti_schedule_provider,
)
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, UserCRUD
from typing import List
from datetime import datetime
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.snippets.sources import eb_datetime


def bisect_left_schedule(
    schedule_dict_list: List[dict],
    today_date: datetime,
) -> int:
    low, high = 0, len(schedule_dict_list)
    index = 0
    while low < high:
        mid = (low + high) // 2
        cur_schedule_date = schedule_dict_list[mid]["time"].date()
        if cur_schedule_date == today_date:
            index = mid
            high = mid - 1
        elif cur_schedule_date < today_date:
            low = mid + 1
        else:
            high = mid - 1

    return index


def bisect_right_schedule(
    schedule_dict_list: List[dict],
    today_date: datetime,
) -> int:
    low, high = 0, len(schedule_dict_list)
    index = high
    while low < high:
        mid = (low + high) // 2
        cur_schedule_date = schedule_dict_list[mid]["time"].date()
        if cur_schedule_date == today_date:
            index = mid + 1
            low = mid + 1
        elif cur_schedule_date < today_date:
            low = mid + 1
        else:
            high = mid

    return index


def add_today_schedule_notification(
    user_email: str,
    schedule_crud: ScheduleCRUD,
    noti_schedule_provider: NotificationScheduleProvider,
):
    schedule_dict_list = schedule_crud.read_all(userEmail=user_email)
    if not schedule_dict_list:
        return

    now = eb_datetime.get_datetime_now()
    now_date = now.date()
    left = bisect_left_schedule(schedule_dict_list, now_date)
    right = bisect_right_schedule(schedule_dict_list, now_date)

    if schedule_dict_list[left]["time"].date() != now_date:
        return

    count = 0
    for i in range(left, right):
        schedule_dict = schedule_dict_list[i]
        notify_schedule = schedule_dict["notify_schedule"]
        if notify_schedule == None:
            continue

        schedule_id = schedule_dict["id"]
        schedule_title = schedule_dict["title"]
        schedule_time = schedule_dict["time"]
        noti_schedule = NotificationSchedule.init(
            user_email=user_email,
            schedule_id=schedule_id,
            schedule_title=schedule_title,
            notify_schedule=notify_schedule,
            schedule_time=schedule_time,
        )

        if noti_schedule == None:
            continue

        count += 1
        noti_schedule_provider.add_schedule(
            noti_schedule=noti_schedule,
        )
    else:
        logger.debug("add_today_schedule_notification")
        logger.debug(f"user_email : {user_email}")
        logger.debug(f"add count : {count}")


def get_all_user(
    user_crud: UserCRUD,
) -> List[dict]:
    return user_crud.read_all()


def empty_and_add_all_user_notification(
    provider=noti_schedule_provider,
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
    all_users = get_all_user(user_crud=user_crud)

    provider.data = []
    for user in all_users:
        user_email = user["email"]
        add_today_schedule_notification(
            user_email=user_email,
            schedule_crud=schedule_crud,
            noti_schedule_provider=noti_schedule_provider,
        )
