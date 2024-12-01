import heapq
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
from typing import List, Optional
from eb_fast_api.snippets.sources import eb_datetime


### 오늘 날짜 일정만 추가 ###


class NotificationScheduleProvider:
    data: List[NotificationSchedule]

    def __init__(self):
        self.data = []

    def __add(
        self,
        noti_schedule: NotificationSchedule,
    ):
        heapq.heappush(self.data, noti_schedule)

    def pop(self) -> NotificationSchedule:
        return heapq.heappop(self.data)

    # remove 알고리즘 개선 n + log n
    def __remove(self, id: str):
        for i, o in enumerate(self.data):
            if o.id == id:
                del self.data[i]
                break
        heapq.heapify(self.data)

    def delete_schedule(
        self,
        id: str,
    ):
        self.__remove(id=id)

    def add_schedule(
        self,
        noti_schedule: NotificationSchedule,
    ):
        self.__add(noti_schedule)

    def get_schedule(self) -> Optional[NotificationSchedule]:
        if not self.data:
            return None

        cur_noti_schedule = self.pop()
        now = eb_datetime.get_datetime_now()
        now_time = eb_datetime.get_only_time(now)

        if now_time == cur_noti_schedule.noti_time:
            return cur_noti_schedule
        else:
            self.__add(cur_noti_schedule)
            return None


noti_schedule_provider = NotificationScheduleProvider()


class NotificationTransportProvider:
    def __init__(self):
        pass
