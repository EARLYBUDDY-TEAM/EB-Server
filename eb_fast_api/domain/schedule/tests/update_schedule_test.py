from eb_fast_api.domain.schedule.sources.schedule_feature.update.update_schedule import (
    update_my_schedule,
)
from eb_fast_api.domain.schema.sources.schemas import (
    ScheduleInfo,
)
from datetime import datetime
from uuid import uuid4


def test_update_schedule(
    schedule_MockUser,
    schedule_MockSession,
    schedule_MockEngine,
    schedule_MockScheduleCRUD,
):
    # create schedule
    schedule_id = str(uuid4())
    scheduleInfo = ScheduleInfo.mock(id=schedule_id)
    schedule = scheduleInfo.toSchedule()
    schedule_MockScheduleCRUD.create(
        userEmail=schedule_MockUser.email,
        schedule=schedule,
    )

    # when
    to_update = scheduleInfo
    timeString = "2024-11-28T05:04:32.299Z"
    time = datetime.fromisoformat(timeString)
    time = time.replace(microsecond=0, tzinfo=None)
    to_update.title = "test_title"
    to_update.memo = "test_memo"
    to_update.notify_schedule = 20
    to_update.notify_transport = 20
    to_update.notify_transport_range = 20
    to_update.time = time
    to_update.startPlaceInfo.id = "test_start_id"
    to_update.endPlaceInfo.id = "test_end_id"

    update_my_schedule(
        engine=schedule_MockEngine,
        session=schedule_MockSession,
        user_email=schedule_MockUser.email,
        schedule_info=to_update,
    )

    fetched_schedule_dict = schedule_MockScheduleCRUD.read(
        user_email=schedule_MockUser.email,
        schedule_id=schedule_id,
    )

    expect_schedule = to_update.toSchedule()
    assert expect_schedule.to_dict() == fetched_schedule_dict
