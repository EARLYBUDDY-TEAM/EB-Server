from unittest.mock import patch
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content as ntc,
)


def patcher_make_subway_notification_body(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        ntc,
        "make_subway_notification_body",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher


def patcher_make_bus_notification_body(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        ntc,
        "make_bus_notification_body",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
