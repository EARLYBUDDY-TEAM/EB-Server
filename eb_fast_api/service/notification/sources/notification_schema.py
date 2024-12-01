from datetime import datetime, timedelta
from eb_fast_api.snippets.sources import eb_datetime
from typing import Optional, Self
from uuid import uuid4


class NotificationSchedule:
    id: str
    user_email: str
    schedule_name: str
    schedule_remain_time: int
    noti_time: datetime  # only time

    def __init__(
        self,
        id: str,
        user_email: str,
        schedule_name: str,
        schedule_remain_time: int,
        noti_time: datetime,
    ):
        self.id = id
        self.user_email = user_email
        self.schedule_name = schedule_name
        self.schedule_remain_time = schedule_remain_time
        self.noti_time = noti_time

    @classmethod
    def init(
        cls,
        user_email: str,
        schedule_id: str,
        schedule_title: str,
        notify_schedule: int,
        schedule_time: datetime,
    ) -> Optional[Self]:
        noti_time = NotificationSchedule.cal_noti_time(
            schedule_time=schedule_time,
            notify_schedule=notify_schedule,
        )
        if noti_time == None:
            return None

        return NotificationSchedule(
            user_email=user_email,
            id=schedule_id,
            schedule_name=schedule_title,
            schedule_remain_time=notify_schedule,
            noti_time=noti_time,
        )

    @classmethod
    def cal_noti_time(
        cls,
        schedule_time: datetime,
        notify_schedule: int,
    ) -> Optional[datetime]:
        noti_time = schedule_time - timedelta(minutes=notify_schedule)
        now = eb_datetime.get_datetime_now()

        if noti_time.date() != now.date():
            return None

        my_noti_time = eb_datetime.get_only_time(noti_time)
        return my_noti_time

    def __lt__(self, other):
        return self.noti_time < other.noti_time

    def __eq__(self, other):
        if other == None:
            return False

        return self.id == other.id

    @classmethod
    def mock(
        cls,
        schedule_remain_time: int = 10,
    ) -> Self:
        id = str(uuid4())
        user_email = "test@test.com"
        schedule_name = "schedule_name"
        schedule_remain_time = schedule_remain_time
        now = eb_datetime.get_datetime_now()
        noti_time = eb_datetime.get_only_time(
            now + timedelta(minutes=schedule_remain_time)
        )

        return NotificationSchedule(
            id=id,
            user_email=user_email,
            schedule_name=schedule_name,
            schedule_remain_time=schedule_remain_time,
            noti_time=noti_time,
        )


class NotificationTransport:
    noti_start_time: datetime
    id: str
