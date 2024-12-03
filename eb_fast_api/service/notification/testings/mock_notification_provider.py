from unittest.mock import patch
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)


def patcher_get_schedule():
    def mock_get_schedule(self):
        cur_noti_schedule = self.pop()
        return [cur_noti_schedule]

    patcher = patch.object(
        NotificationScheduleProvider,
        "get_schedule",
        new=mock_get_schedule,
    )
    return patcher
