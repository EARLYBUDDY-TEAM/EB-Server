from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD
from unittest.mock import patch


def mock_def_create_schedule_SUCCESS(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_create_schedule_SUCCESS !!!")
    return


def mock_create_schedule_SUCCESS():
    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.createSchedule",
        new=mock_def_create_schedule_SUCCESS,
    ).start()


def mock_def_create_schedule_FAIL(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_create_schedule_FAIL !!!")
    raise Exception()


def mock_create_schedule_FAIL():
    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.createSchedule",
        new=mock_def_create_schedule_FAIL,
    ).start()


def mock_def_update_schedule_with_info_SUCCESS(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_def_update_schedule_with_info_SUCCESS !!!")
    return


def mock_update_schedule_with_info_SUCCESS():
    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.update_schedule_with_info",
        new=mock_def_update_schedule_with_info_SUCCESS,
    ).start()


def mock_def_update_schedule_with_info_FAIL(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_def_update_schedule_with_info_FAIL !!!")
    raise Exception()


def mock_update_schedule_with_info_FAIL():
    patch(
        "eb_fast_api.domain.schedule.sources.schedule_feature.update_schedule_with_info",
        new=mock_def_update_schedule_with_info_FAIL,
    ).start()