from eb_fast_api.domain.schema.sources.schema import (
    RegisterInfo,
    PlaceInfo,
    ScheduleInfo,
)
from eb_fast_api.database.sources.model.models import Schedule, Place
from eb_fast_api.domain.home.sources import home_feature


def test_read_all_schedule(
    home_MockUserCRUD,
    home_MockScheduleCRUD,
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
            startPlace=None,
            endPlace=None,
        )
        home_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule2,
            startPlace=None,
            endPlace=None,
        )
        home_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule3,
            startPlace=None,
            endPlace=None,
        )

        # when
        fetched_schedule_dict_list = home_feature.read_all_schedule(
            userEmail=user.email,
            scheduleCRUD=home_MockScheduleCRUD,
        )

        # then
        assert len(fetched_schedule_dict_list) == 3

    # delete schedule table
    finally:
        home_MockScheduleCRUD.dropTable(userEmail=email)


def test_get_placeinfo_from_id_When_PlaceID_is_None(
    home_MockPlaceCRUD,
):
    # given
    placeID = None

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        placeID=placeID,
        placeCRUD=home_MockPlaceCRUD,
    )

    # then
    assert placeInfo == None


def test_get_placeinfo_from_id_When_No_Place_Data(
    home_MockPlaceCRUD,
):
    # given
    placeID = "placeID"

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        placeID=placeID,
        placeCRUD=home_MockPlaceCRUD,
    )

    # then
    assert placeInfo == None


def test_get_placeinfo_from_id_SUCCESS(
    home_MockPlaceCRUD,
):
    # given
    placeID = "placeID"
    mockPlace = Place.mock(id=placeID)
    home_MockPlaceCRUD.create(place=mockPlace)

    # when
    placeInfo = home_feature.get_placeinfo_from_id(
        placeID=placeID,
        placeCRUD=home_MockPlaceCRUD,
    )

    # then
    expectPlaceInfo = PlaceInfo.fromPlaceDict(place_dict=mockPlace.to_dict())
    assert placeInfo == expectPlaceInfo


def test_schedule_dict_to_schedule_info(
    home_MockPlaceCRUD,
):
    # given
    mockSchedule = Schedule.mock(id=10)
    mockSchedule.startPlaceID = None
    mockSchedule.endPlaceID = None

    # when
    scheduleInfo = home_feature.schedule_dict_to_schedule_info(
        schedule_dict=mockSchedule.to_dict(),
        placeCRUD=home_MockPlaceCRUD,
    )

    # then
    expectScheduleInfo = ScheduleInfo(
        id=mockSchedule.id,
        title=mockSchedule.title,
        memo=mockSchedule.memo,
        time=mockSchedule.time,
        isNotify=mockSchedule.isNotify,
        startPlaceInfo=None,
        endPlaceInfo=None,
    )

    print(scheduleInfo)
    print(expectScheduleInfo)

    assert scheduleInfo == expectScheduleInfo
