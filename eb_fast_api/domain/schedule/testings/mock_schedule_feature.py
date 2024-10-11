from eb_fast_api.domain.schedule.sources.schedule_schema import AddScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def mock_create_schedule_SUCCESS(
    userEmail: str,
    addScheduleInfo: AddScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_create_schedule_SUCCESS !!!")
    return


def mock_create_schedule_FAIL(
    userEmail: str,
    addScheduleInfo: AddScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    print("mock_create_schedule_FAIL !!!")
    raise Exception()
