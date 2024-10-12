from unittest.mock import patch
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.home.sources.home_schema import ScheduleSchema
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD
from typing import List


scheduleCount = 5
mockScheduleList = [Schedule.mockWithID() for _ in range(scheduleCount)]
mockScheduleSchema = ScheduleSchema.mock()


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


def mock_def_schedule_to_schedule_schema(
    schedule: Schedule,
    placeCRUD: PlaceCRUD,
) -> ScheduleSchema:
    return mockScheduleSchema


def mock_schedule_to_schedule_schema():
    patch(
        "eb_fast_api.domain.home.sources.home_feature.schedule_to_schedule_schema",
        new=mock_def_schedule_to_schedule_schema,
    ).start()