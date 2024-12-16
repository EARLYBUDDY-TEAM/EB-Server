from unittest.mock import patch
from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    add_notification_to_provider as antp,
)


def patcher_prepare_add_noti_transport_to_provider(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        antp,
        "prepare_add_noti_transport_to_provider",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher


def patcher_add_notification_transport_to_provider(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        antp,
        "add_notification_transport_to_provider",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher


def patcher_add_notification_schedule_to_provider(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        antp,
        "add_notification_schedule_to_provider",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher


def patcher_prepare_add_noti_transport_to_provider(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        antp,
        "prepare_add_noti_transport_to_provider",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher
