from eb_fast_api.domain.schema.sources.schema import RegisterInfo
from eb_fast_api.database.sources.model.models import Schedule, Place
from eb_fast_api.domain.home.sources import home_feature


def test_read_all_schedule(
    home_MockUserCRUD,
    home_MockScheduleCRUD,
):
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
    scheduleList = home_feature.read_all_schedule(
        userEmail=user.email,
        scheduleCRUD=home_MockScheduleCRUD,
    )

    # then
    assert len(scheduleList) == 3

    # delete schedule table
    home_MockScheduleCRUD.dropTable(userEmail=email)


def test_schedule_to_schedulecard(
    home_MockPlaceCRUD,
):
    # given
    mockPlace = Place.mock()
    home_MockPlaceCRUD.create(place=mockPlace)
    mockSchedule = Schedule.mock()
    mockSchedule.id = 10
    mockSchedule.endPlaceID = mockPlace.id

    # when
    scheduleCard = home_feature.schedule_to_schedulecard(
        schedule=mockSchedule,
        placeCRUD=home_MockPlaceCRUD,
    )

    # then
    assert scheduleCard.scheduleID == mockSchedule.id
    assert scheduleCard.title == mockSchedule.title
    assert scheduleCard.time == mockSchedule.time
    assert scheduleCard.endPlaceName == mockPlace.name
