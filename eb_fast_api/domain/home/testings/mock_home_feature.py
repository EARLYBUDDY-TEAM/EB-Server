from unittest.mock import patch
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.home.sources.home_schema import ScheduleInfoList
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD
from typing import List


scheduleCount = 5
mockScheduleList = [Schedule.mockWithID() for _ in range(scheduleCount)]
mockScheduleInfo = ScheduleInfo.mockWithID()


def mock_def_read_all_schedule(
    userEmail: str,
    scheduleCRUD: ScheduleCRUD,
) -> List[Schedule]:
    return mockScheduleList


def mock_read_all_schedule():
    patch(
        "eb_fast_api.domain.home.sources.home_feature.read_all_schedule",
        new=mock_def_read_all_schedule,
    ).start()


def mock_def_schedule_to_schedule_info(
    schedule: Schedule,
    placeCRUD: PlaceCRUD,
) -> ScheduleInfoList:
    return mockScheduleInfo


def mock_schedule_to_schedule_info():
    patch(
        "eb_fast_api.domain.home.sources.home_feature.schedule_to_schedule_info",
        new=mock_def_schedule_to_schedule_info,
    ).start()
