from unittest.mock import patch
from typing import List
from sqlalchemy.orm import Session

from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.home.sources.home_schema import SchedulePathInfo
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD
from uuid import uuid4


scheduleCount = 5
mockScheduleList = [Schedule.mock() for index in range(scheduleCount)]

schedule_id = str(uuid4())
mockSchedulePathInfo = SchedulePathInfo.mock(id=schedule_id)


def mock_read_all_schedule():
    def mock_def_read_all_schedule(
        userEmail: str,
        session: Session,
    ) -> List[Schedule]:
        return mockScheduleList

    patch(
        "eb_fast_api.domain.home.sources.home_feature.read_all_schedule",
        new=mock_def_read_all_schedule,
    ).start()


def mock_schedule_dict_to_schedule_path_info():
    def mock_def_schedule_dict_to_schedule_path_info(
        session: Session,
        user_email: str,
        schedule_dict: dict,
    ) -> SchedulePathInfo:
        return mockSchedulePathInfo

    patch(
        "eb_fast_api.domain.home.sources.home_feature.schedule_dict_to_schedule_path_info",
        new=mock_def_schedule_dict_to_schedule_path_info,
    ).start()
