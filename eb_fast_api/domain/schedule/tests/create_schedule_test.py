from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_schedule as cs,
)
from eb_fast_api.domain.schema.sources.schemas import (
    RegisterInfo,
    ScheduleInfo,
    PlaceInfo,
    PathInfo,
)
from uuid import uuid4


def test_create_path(
    schedule_MockPathCRUD,
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockSession,
):
    try:
        # given
        email = "email"
        password = "password"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
        schedule_MockUserCRUD.create(user=user)

        # when
        path_id = str(uuid4())
        path_info = PathInfo.mock()
        cs.create_path(
            session=schedule_MockSession,
            user_email=user.email,
            path_id=path_id,
            path_info=path_info,
        )

        # then
        fetched_path_dict = schedule_MockPathCRUD.read(
            user_email=user.email, path_id=path_id
        )
        assert fetched_path_dict["data"] == path_info.model_dump(mode="json")

    # delete path, schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=user.email)
        schedule_MockPathCRUD.dropTable(user_email=user.email)


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
    schedule_MockSession,
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPathCRUD,
):
    try:
        # given
        email = "email"
        password = "password"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
        schedule_MockUserCRUD.create(user)
        schedule_id = str(uuid4())
        scheduleInfo = ScheduleInfo.mock()
        scheduleInfo.id = None

        # when
        cs.create_my_schedule(
            session=schedule_MockSession,
            user_email=user.email,
            schedule_id=schedule_id,
            schedule_info=scheduleInfo,
        )

        # then
        fetched_schedule_dict = schedule_MockScheduleCRUD.read(
            user_email=user.email,
            schedule_id=schedule_id,
        )
        schedule = scheduleInfo.toSchedule(id=schedule_id)
        assert schedule.to_dict() == fetched_schedule_dict

    # delete path, schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
        schedule_MockPathCRUD.dropTable(user_email=email)
