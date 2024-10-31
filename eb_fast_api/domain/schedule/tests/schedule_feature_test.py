from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schemas import (
    RegisterInfo,
    ScheduleInfo,
    PlaceInfo,
    PathInfo,
)
from eb_fast_api.database.sources.model.models import Schedule
from datetime import datetime
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
        schedule_feature.create_path(
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
    schedule_feature.create_place(
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
        schedule_feature.create_my_schedule(
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


def test_update_schedule(
    schedule_MockSession,
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPathCRUD,
):
    try:
        # given
        # create user
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

        # create schedule
        schedule_id = str(uuid4())
        scheduleInfo = ScheduleInfo.mock(id=schedule_id)
        schedule = scheduleInfo.toSchedule()
        schedule_MockScheduleCRUD.create(
            userEmail=user.email,
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

        schedule_feature.update_my_schedule(
            session=schedule_MockSession,
            user_email=user.email,
            schedule_info=to_update,
        )

        fetched_schedule_dict = schedule_MockScheduleCRUD.read(
            user_email=user.email,
            schedule_id=schedule_id,
        )

        expect_schedule = to_update.toSchedule()
        assert expect_schedule.to_dict() == fetched_schedule_dict

    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
        schedule_MockPathCRUD.dropTable(user_email=email)


def test_delete_schedule(
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
        schedule_MockUserCRUD.create(user=user)

        path_info = PathInfo.mock()
        schedule_id = str(uuid4())
        schedule = Schedule.mock(id=schedule_id)
        schedule_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule,
        )
        path = path_info.to_path(id=schedule_id)
        schedule_MockPathCRUD.create(
            user_email=user.email,
            path=path,
        )

        # when
        schedule_feature.delete_schedule(
            session=schedule_MockSession,
            user_email=user.email,
            schedule_id=schedule_id,
        )

        # then
        try:
            schedule_MockScheduleCRUD.read(
                user_email=user.email, schedule_id=schedule_id
            )
            raise Exception("test_delete_schedule_fail")
        except:
            pass

        fetched_path_dict = schedule_MockPathCRUD.read(
            user_email=user.email,
            path_id=schedule_id,
        )
        if fetched_path_dict:
            raise Exception("test_delete_schedule_fail")
        else:
            return
    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
        schedule_MockPathCRUD.dropTable(user_email=email)
