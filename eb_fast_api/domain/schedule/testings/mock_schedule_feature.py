from unittest.mock import patch
from sqlalchemy.orm import Session
from typing import Optional

from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def mock_create_schedule_SUCCESS():
    def mock_def_create_schedule_SUCCESS(
        session: Session,
        userEmail: str,
        scheduleInfo: ScheduleInfo,
        pathInfo: Optional[PathInfo],
    ):
        print("mock_create_schedule_SUCCESS !!!")
        return

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.create_schedule",
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

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.create_schedule",
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

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.update_schedule",
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

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.update_schedule",
        new=mock_def_update_schedule_FAIL,
    ).start()


def mock_delete_schedule_SUCCESS():
    def mock_def_delete_schedule_SUCCESS(
        session: Session,
        user_email: str,
        schedule_id: str,
    ):
        return

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.delete_schedule",
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

    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.delete_schedule",
        new=mock_def_delete_schedule_FAIL,
    ).start()
