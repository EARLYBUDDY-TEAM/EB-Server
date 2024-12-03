import heapq
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
from typing import List
from eb_fast_api.snippets.sources import eb_datetime
from datetime import datetime

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

    def get_schedule(
        self,
        now: datetime = eb_datetime.get_datetime_now(),
    ) -> List[NotificationSchedule]:
        noti_schedule_list = []
        now_time = eb_datetime.get_only_time(now)

        while self.data:
            cur_noti_schedule = self.pop()
            noti_time = cur_noti_schedule.noti_time

            if now_time == noti_time:
                noti_schedule_list.append(cur_noti_schedule)
            elif now_time < noti_time:
                self.__add(cur_noti_schedule)
                break

        return noti_schedule_list


noti_schedule_provider = NotificationScheduleProvider()


class NotificationTransportProvider:
    def __init__(self):
        pass
