import heapq
from abc import ABC, abstractmethod
from eb_fast_api.snippets.sources import eb_datetime
from datetime import datetime


class NotificationProvider(ABC):
    data: list

    def __init__(self):
        self.data = []

    def add(
        self,
        noti_schedule,
    ):
        heapq.heappush(self.data, noti_schedule)

    def pop(self):
        return heapq.heappop(self.data)

    # remove 알고리즘 개선 n + log n
    def remove(self, schedule_id):
        for i, o in enumerate(self.data):
            if o.schedule_id == schedule_id:
                del self.data[i]
                break
        heapq.heapify(self.data)

    def delete_schedule(
        self,
        schedule_id,
    ):
        self.remove(schedule_id=schedule_id)

    @abstractmethod
    def add_schedule(
        self,
        noti_schedule,
        now,
    ):
        pass

    @abstractmethod
    def get_schedule(
        self,
        now: datetime,
    ):
        pass
