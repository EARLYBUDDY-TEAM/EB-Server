from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_schedule as cs,
)
from eb_fast_api.domain.schema.sources.schemas import (
    ScheduleInfo,
    PlaceInfo,
    PathInfo,
)
from uuid import uuid4


def test_create_path(
    schedule_MockPathCRUD,
    schedule_MockSession,
    schedule_MockUser,
):
    # given
    path_id = str(uuid4())
    path_info = PathInfo.mock()

    # when
    cs.create_path(
        session=schedule_MockSession,
        user_email=schedule_MockUser.email,
        path_id=path_id,
        path_info=path_info,
    )

    # then
    fetched_path_dict = schedule_MockPathCRUD.read(
        user_email=schedule_MockUser.email,
        path_id=path_id,
    )
    assert fetched_path_dict["data"] == path_info.model_dump(mode="json")


def test_create_place(
    schedule_MockSession,
    schedule_MockPlaceCRUD,
):
    # given
    place_info = PlaceInfo.mock()

    # when
    cs.create_place(
        session=schedule_MockSession,
        place_info=place_info,
    )

    fetched_place_dict = schedule_MockPlaceCRUD.read(place_id=place_info.id)
    fetched_place_dict["refCount"] = None
    assert fetched_place_dict == place_info.toPlace().to_dict()


def test_create_my_schedule(
    schedule_MockUser,
    schedule_MockSession,
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPathCRUD,
):
    # given
    schedule_id = str(uuid4())
    scheduleInfo = ScheduleInfo.mock()
    scheduleInfo.id = None

    # when
    cs.create_my_schedule(
        session=schedule_MockSession,
        user_email=schedule_MockUser.email,
        schedule_id=schedule_id,
        schedule_info=scheduleInfo,
    )

    # then
    fetched_schedule_dict = schedule_MockScheduleCRUD.read(
        user_email=schedule_MockUser.email,
        schedule_id=schedule_id,
    )
    schedule = scheduleInfo.toSchedule(id=schedule_id)
    assert schedule.to_dict() == fetched_schedule_dict
