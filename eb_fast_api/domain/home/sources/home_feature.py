from typing import List
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def read_all_schedule(
    userEmail: str,
    scheduleCRUD: ScheduleCRUD,
) -> List[Schedule]:
    fetchedScheduleList = scheduleCRUD.read_all(userEmail=userEmail)
    return fetchedScheduleList
