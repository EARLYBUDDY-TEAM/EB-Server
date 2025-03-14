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
    schedule_MockEngine,
):
    # given
    path_id = str(uuid4())
    path_info = PathInfo.mock()

    # when
    cs.create_path(
        session=schedule_MockSession,
        engine=schedule_MockEngine,
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
    schedule_MockEngine,
):
    # given
    place_info = PlaceInfo.mock()

    # when
    cs.create_place(
        session=schedule_MockSession,
        engine=schedule_MockEngine,
        place_info=place_info,
    )

    fetched_place_dict = schedule_MockPlaceCRUD.read(place_id=place_info.id)
    fetched_place_dict["refCount"] = None
    assert fetched_place_dict == place_info.toPlace().to_dict()


def test_create_my_schedule(
    schedule_MockUser,
    schedule_MockSession,
    schedule_MockScheduleCRUD,
    schedule_MockEngine,
):
    # given
    scheduleInfo = ScheduleInfo.mock(id=str(uuid4()))

    # when
    cs.create_my_schedule(
        session=schedule_MockSession,
        engine=schedule_MockEngine,
        user_email=schedule_MockUser.email,
        schedule_info=scheduleInfo,
    )

    # then
    fetched_schedule_dict = schedule_MockScheduleCRUD.read(
        user_email=schedule_MockUser.email,
        schedule_id=scheduleInfo.id,
    )
    schedule = scheduleInfo.toSchedule()
    assert schedule.to_dict() == fetched_schedule_dict
