from eb_fast_api.database.sources.model.models import Schedule, Place, User


def test_scheduleCreate(mockSession, mockUserCRUD, mockScheduleCRUD):
    # given
    email = "email"
    user = User.mock(email=email)
    mockUserCRUD.create(user=user)
    schedule = Schedule.mock()
    startPlace = Place.mock(id="mockStartPlace")
    endPlace = Place.mock(id="mockEndPlace")
    schedule.startPlaceID = startPlace.id
    schedule.endPlaceID = endPlace.id

    # when
    mockScheduleCRUD.create(
        userEmail=email,
        schedule=schedule,
        startPlace=startPlace,
        endPlace=endPlace,
    )

    # then
    placeCount = mockSession.query(Place).count()
    assert placeCount == 2

    scheduleTable = Schedule.getTable(email=user.email)
    scheduleCount = mockSession.query(scheduleTable).count()
    assert scheduleCount == 1

    # teardown
    mockScheduleCRUD.dropAll(userEmail=user.email)
