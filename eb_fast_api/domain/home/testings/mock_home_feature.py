from unittest.mock import patch
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD
from typing import List


scheduleCount = 5
mockScheduleList = [Schedule.mockWithID() for _ in range(scheduleCount)]


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


# scheduleCount = 5
# mockScheduleList = [Schedule.mock() for _ in range(scheduleCount)]
# mockSchedulCard = ScheduleCard.mock()


# def mock_read_all_schedule(
#     userEmail: str,
#     scheduleCRUD: ScheduleCRUD,
# ) -> List[Schedule]:
#     return mockScheduleList


# def mock_schedule_to_schedulecard(
#     schedule: Schedule,
#     placeCRUD: PlaceCRUD,
# ) -> ScheduleCard:
#     return mockSchedulCard


# def mocking_home_feature():
#     patch(
#         "eb_fast_api.domain.home.sources.home_feature.read_all_schedule",
#         new=mock_read_all_schedule,
#     ).start()
#     patch(
#         "eb_fast_api.domain.home.sources.home_feature.schedule_to_schedulecard",
#         new=mock_schedule_to_schedulecard,
#     ).start()
