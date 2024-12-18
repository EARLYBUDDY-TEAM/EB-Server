from unittest.mock import patch
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)


def patcher_init(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        NotificationSchedule,
        "init",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
