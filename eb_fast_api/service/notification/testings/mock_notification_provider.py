from unittest.mock import patch
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from datetime import datetime


def patcher_get_schedule():
    def mock_get_schedule(
        self,
        now: datetime,
    ):
        cur_noti_schedule = self.pop()
        return [cur_noti_schedule]

    patcher = patch.object(
        NotificationScheduleProvider,
        "get_schedule",
        new=mock_get_schedule,
    )
    return patcher
