from datetime import datetime
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.notification.sources.provider.notification_provider import (
    NotificationProvider,
)


class NotificationTransportProvider(NotificationProvider):
    def add_notification(
        self,
        noti_schedule,
        now,
    ):
        now_time = eb_datetime.get_only_time(now)
        if noti_schedule.noti_end_time < now_time:
            return

        self.add(noti_schedule)

    def get_notification(
        self,
        now: datetime,
    ):
        noti_transport_list = []
        now_time = eb_datetime.get_only_time(now)

        while self.data:
            cur_noti_transport = self.pop()
            noti_start_time = cur_noti_transport.noti_start_time
            noti_end_time = cur_noti_transport.noti_end_time

            if noti_start_time <= now_time <= noti_end_time:
                noti_transport_list.append(cur_noti_transport)
            elif now_time < noti_end_time:
                self.add(cur_noti_transport)
                break

        return noti_transport_list


noti_transport_provider = NotificationTransportProvider()
