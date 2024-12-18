from unittest.mock import patch
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content_helper as ntch,
)


def patcher_get_arrival_info(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        ntch,
        "get_arrival_info",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
