from unittest.mock import patch
from sqlalchemy.orm import Session
from typing import Optional

from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.domain.schedule.sources import schedule_router
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)


def mock_create_notification_schedule_SUCCESS():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        print("mock_create_notification_schedule_SUCCESS !!!")
        return

    patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        new=mock_def,
    ).start()


def mock_create_notification_schedule_FAIL():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        print("mock_create_notification_schedule_FAIL !!!")
        raise Exception()

    patch.object(
        schedule_router.cns,
        "create_notification_schedule",
        new=mock_def,
    ).start()


def mock_update_notification_schedule_SUCCESS():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        return

    patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        new=mock_def,
    ).start()


def mock_update_notification_schedule_FAIL():
    def mock_def(
        user_email: str,
        schedule_info: ScheduleInfo,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        raise Exception()

    patch.object(
        schedule_router.uns,
        "update_notification_schedule",
        new=mock_def,
    ).start()


def mock_delete_notification_schedule_SUCCESS():
    def mock_def(
        schedule_id: str,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        return

    patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        new=mock_def,
    ).start()


def mock_delete_notification_schedule_FAIL():
    def mock_def(
        schedule_id: str,
        noti_schedule_provider: NotificationScheduleProvider,
    ):
        raise Exception()

    patch.object(
        schedule_router.dns,
        "delete_notification_schedule",
        new=mock_def,
    ).start()


def mock_create_schedule_SUCCESS():
    def mock_def_create_schedule_SUCCESS(
        session: Session,
        userEmail: str,
        scheduleInfo: ScheduleInfo,
        pathInfo: Optional[PathInfo],
    ):
        print("mock_create_schedule_SUCCESS !!!")
        return

    patch.object(
        schedule_router.cs,
        "create_schedule",
        new=mock_def_create_schedule_SUCCESS,
    ).start()


def mock_create_schedule_FAIL():
    def mock_def_create_schedule_FAIL(
        session: Session,
        userEmail: str,
        scheduleInfo: ScheduleInfo,
        pathInfo: Optional[PathInfo],
    ):
        print("mock_create_schedule_FAIL !!!")
        raise Exception()

    patch.object(
        schedule_router.cs,
        "create_schedule",
        new=mock_def_create_schedule_FAIL,
    ).start()


def mock_update_schedule_SUCCESS():
    def mock_def_update_schedule_SUCCESS(
        session: Session,
        userEmail: str,
        scheduleInfo: ScheduleInfo,
        pathInfo: Optional[PathInfo],
    ):
        print("mock_def_update_schedule_SUCCESS !!!")
        return

    patch.object(
        schedule_router.us,
        "update_schedule",
        new=mock_def_update_schedule_SUCCESS,
    ).start()


def mock_update_schedule_FAIL():
    def mock_def_update_schedule_FAIL(
        session: Session,
        userEmail: str,
        scheduleInfo: ScheduleInfo,
        pathInfo: Optional[PathInfo],
    ):
        print("mock_def_update_schedule_FAIL !!!")
        raise Exception()

    patch.object(
        schedule_router.us,
        "update_schedule",
        new=mock_def_update_schedule_FAIL,
    ).start()


def mock_delete_schedule_SUCCESS():
    def mock_def_delete_schedule_SUCCESS(
        session: Session,
        user_email: str,
        schedule_id: str,
    ):
        return

    patch.object(
        schedule_router.ds,
        "delete_schedule",
        new=mock_def_delete_schedule_SUCCESS,
    ).start()


def mock_delete_schedule_FAIL():
    def mock_def_delete_schedule_FAIL(
        session: Session,
        user_email: str,
        schedule_id: str,
    ):
        raise Exception("mock_delete_schedule_FAIL")
        return

    patch.object(
        schedule_router.ds,
        "delete_schedule",
        new=mock_def_delete_schedule_FAIL,
    ).start()
