from eb_fast_api.domain.schema.sources.schemas import (
    RegisterInfo,
    PlaceInfo,
    ScheduleInfo,
    PathInfo,
)
from eb_fast_api.database.sources.model.models import Schedule, Place
from eb_fast_api.domain.home.sources import home_feature
from uuid import uuid4


def test_read_all_schedule(
    home_MockSession,
    home_MockUserCRUD,
    home_MockScheduleCRUD,
    home_MockPathCRUD,
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
        home_MockUserCRUD.create(user)

        schedule1 = Schedule.mock(title="mock1")
        schedule2 = Schedule.mock(title="mock2")
        schedule3 = Schedule.mock(title="mock3")
        home_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule1,
        )
        home_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule2,
        )
        home_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule3,
        )

        # when
        fetched_schedule_dict_list = home_feature.read_all_schedule(
            session=home_MockSession,
            userEmail=user.email,
        )

        # then
        assert len(fetched_schedule_dict_list) == 3

    # delete schedule table
    finally:
        home_MockScheduleCRUD.dropTable(userEmail=email)
        home_MockPathCRUD.dropTable(user_email=email)


def test_get_placeinfo_from_id_When_PlaceID_is_None(
    home_MockSession,
):
    # given
    placeID = None

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        session=home_MockSession,
        placeID=placeID,
    )

    # then
    assert placeInfo == None


def test_get_placeinfo_from_id_When_No_Place_Data(
    home_MockSession,
):
    # given
    placeID = "placeID"

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        session=home_MockSession,
        placeID=placeID,
    )

    # then
    assert placeInfo == None


def test_get_placeinfo_from_id_SUCCESS(
    home_MockPlaceCRUD,
    home_MockSession,
):
    # given
    placeID = "placeID"
    mockPlace = Place.mock(id=placeID)
    home_MockPlaceCRUD.create(place=mockPlace)

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        session=home_MockSession,
        placeID=placeID,
    )

    # then
    expectPlaceInfo = PlaceInfo.fromPlaceDict(place_dict=mockPlace.to_dict())
    assert placeInfo == expectPlaceInfo


def test_get_schedule_info_from_dict(
    home_MockSession,
):
    # given
    schedule_id = str(uuid4())
    mockSchedule = Schedule.mock(id=schedule_id)
    mockSchedule.startPlaceID = None
    mockSchedule.endPlaceID = None

    # when
    scheduleInfo = home_feature.get_schedule_info_from_dict(
        session=home_MockSession,
        schedule_dict=mockSchedule.to_dict(),
    )

    # then
    expectScheduleInfo = ScheduleInfo(
        id=mockSchedule.id,
        title=mockSchedule.title,
        memo=mockSchedule.memo,
        time=mockSchedule.time,
        notify_schedule=mockSchedule.notify_schedule,
        notify_transport=mockSchedule.notify_transport,
        notify_transport_range=mockSchedule.notify_transport_range,
        startPlaceInfo=None,
        endPlaceInfo=None,
    )

    assert scheduleInfo == expectScheduleInfo


def test_get_path_info(
    home_MockSession,
    home_MockPathCRUD,
    home_MockScheduleCRUD,
    home_MockUserCRUD,
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
        home_MockUserCRUD.create(user=user)

        path_info = PathInfo.mock()
        schedule_id = str(uuid4())
        path = path_info.to_path(id=schedule_id)
        home_MockPathCRUD.create(user_email=user.email, path=path)

        # when
        fetched_path_info = home_feature.get_path_info(
            session=home_MockSession,
            user_email=user.email,
            schedule_id=schedule_id,
        )

        # then
        assert path_info == fetched_path_info

    # delete schedule table
    finally:
        home_MockScheduleCRUD.dropTable(userEmail=email)
        home_MockPathCRUD.dropTable(user_email=email)
