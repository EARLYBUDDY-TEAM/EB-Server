from unittest.mock import patch
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.home.sources.home_schema import ScheduleInfoList
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD
from typing import List


scheduleCount = 5
mockScheduleList = [Schedule.mock(id=index) for index in range(scheduleCount)]
mockScheduleInfo = ScheduleInfo.mock()


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


def mock_def_schedule_dict_to_schedule_info(
    schedule_dict: dict,
    placeCRUD: PlaceCRUD,
) -> ScheduleInfoList:
    return mockScheduleInfo


def mock_schedule_dict_to_schedule_info():
    patch(
        "eb_fast_api.domain.home.sources.home_feature.schedule_dict_to_schedule_info",
        new=mock_def_schedule_dict_to_schedule_info,
    ).start()
