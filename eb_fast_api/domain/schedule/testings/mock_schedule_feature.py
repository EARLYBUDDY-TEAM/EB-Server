from unittest.mock import patch
from sqlalchemy.orm import Session
from sqlalchemy import Engine
from typing import Optional

from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.domain.schedule.sources import schedule_router
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)


def patcher_create_notification_schedule_SUCCESS():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        print("mock_create_notification_schedule_SUCCESS !!!")
        return

    patcher = patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_create_notification_schedule_FAIL():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        print("mock_create_notification_schedule_FAIL !!!")
        raise Exception()

    patcher = patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_update_notification_schedule_SUCCESS():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        return

    patcher = patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_update_notification_schedule_FAIL():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        raise Exception()

    patcher = patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_delete_notification_schedule_SUCCESS():
    def mock_def(
        schedule_id: str,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        return

    patcher = patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_delete_notification_schedule_FAIL():
    def mock_def(
        schedule_id: str,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        raise Exception()

    patcher = patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        new=mock_def,
    )

    return patcher


def patcher_create_schedule_SUCCESS():
    def mock_def_create_schedule_SUCCESS(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_info: ScheduleInfo,
        path_info: Optional[PathInfo],
    ):
        print("mock_create_schedule_SUCCESS !!!")
        return

    patcher = patch.object(
        schedule_router.cs,
        "create_schedule",
        new=mock_def_create_schedule_SUCCESS,
    )

    return patcher


def patcher_create_schedule_FAIL():
    def mock_def_create_schedule_FAIL(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_info: ScheduleInfo,
        path_info: Optional[PathInfo],
    ):
        print("mock_create_schedule_FAIL !!!")
        raise Exception()

    patcher = patch.object(
        schedule_router.cs,
        "create_schedule",
        new=mock_def_create_schedule_FAIL,
    )

    return patcher


def patcher_update_schedule_SUCCESS():
    def mock_def_update_schedule_SUCCESS(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_info: ScheduleInfo,
        path_info: Optional[PathInfo],
    ):
        print("mock_def_update_schedule_SUCCESS !!!")
        return

    patcher = patch.object(
        schedule_router.us,
        "update_schedule",
        new=mock_def_update_schedule_SUCCESS,
    )

    return patcher


def patcher_update_schedule_FAIL():
    def mock_def_update_schedule_FAIL(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_info: ScheduleInfo,
        path_info: Optional[PathInfo],
    ):
        print("mock_def_update_schedule_FAIL !!!")
        raise Exception()

    patcher = patch.object(
        schedule_router.us,
        "update_schedule",
        new=mock_def_update_schedule_FAIL,
    )

    return patcher


def patcher_delete_schedule_SUCCESS():
    def mock_def_delete_schedule_SUCCESS(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_id: str,
    ):
        return

    patcher = patch.object(
        schedule_router.ds,
        "delete_schedule",
        new=mock_def_delete_schedule_SUCCESS,
    )

    return patcher


def patcher_delete_schedule_FAIL():
    def mock_def_delete_schedule_FAIL(
        session: Session,
        engine: Engine,
        user_email: str,
        schedule_id: str,
    ):
        raise Exception("mock_delete_schedule_FAIL")
        return

    patcher = patch.object(
        schedule_router.ds,
        "delete_schedule",
        new=mock_def_delete_schedule_FAIL,
    )

    return patcher
