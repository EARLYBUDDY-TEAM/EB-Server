from datetime import datetime
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.notification.sources.provider.notification_provider import (
    NotificationProvider,
)


class NotificationScheduleProvider(NotificationProvider):
    def add_notification(
        self,
        noti_schedule,
        now,
    ):
        now_time = eb_datetime.get_only_time(now)
        if noti_schedule.noti_time < now_time:
            return

        self.add(noti_schedule)

    def get_notification(
        self,
        now: datetime,
    ):
        noti_schedule_list = []
        now_time = eb_datetime.get_only_time(now)

        while self.data:
            cur_noti_schedule = self.pop()
            noti_time = cur_noti_schedule.noti_time

            if now_time == noti_time:
                noti_schedule_list.append(cur_noti_schedule)
            elif now_time < noti_time:
                self.add(cur_noti_schedule)
                break

        return noti_schedule_list


noti_schedule_provider = NotificationScheduleProvider()
