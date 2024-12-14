from unittest.mock import patch
from eb_fast_api.domain.schedule.sources import schedule_router


def patcher_create_notification_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        return_value=None,
    )

    return patcher


def patcher_create_notification_schedule_FAIL():
    patcher = patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        side_effect=Exception("mock_create_notification_schedule_FAIL"),
    )

    return patcher


def patcher_update_notification_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        return_value=None,
    )

    return patcher


def patcher_update_notification_schedule_FAIL():
    patcher = patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        side_effect=Exception("patcher_update_notification_schedule_FAIL"),
    )

    return patcher


def patcher_delete_notification_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        return_value=None,
    )

    return patcher


def patcher_delete_notification_schedule_FAIL():
    patcher = patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        side_effect=Exception("patcher_delete_notification_schedule_FAIL"),
    )

    return patcher


def patcher_create_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.cs,
        "create_schedule",
        return_value=None,
    )

    return patcher


def patcher_create_schedule_FAIL():
    patcher = patch.object(
        schedule_router.cs,
        "create_schedule",
        side_effect=Exception("patcher_create_schedule_FAIL"),
    )

    return patcher


def patcher_update_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.us,
        "update_schedule",
        return_value=None,
    )

    return patcher


def patcher_update_schedule_FAIL():
    patcher = patch.object(
        schedule_router.us,
        "update_schedule",
        side_effect=Exception("patcher_update_schedule_FAIL"),
    )

    return patcher


def patcher_delete_schedule_SUCCESS():
    patcher = patch.object(
        schedule_router.ds,
        "delete_schedule",
        return_value=None,
    )

    return patcher


def patcher_delete_schedule_FAIL():
    patcher = patch.object(
        schedule_router.ds,
        "delete_schedule",
        side_effect=Exception("patcher_delete_schedule_FAIL"),
    )

    return patcher
