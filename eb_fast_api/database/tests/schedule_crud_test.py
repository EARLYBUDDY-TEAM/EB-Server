from eb_fast_api.database.sources.model.models import Schedule, Place, User
from sqlalchemy.engine.row import Row


def test_schedule_create_and_read_all(
    mockSession,
    mockUserCRUD,
    mockScheduleCRUD,
):
    try:
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
        # assert place
        fetchedPlaceList = mockSession.query(Place).all()
        fetchedAllPlace = set(fetchedPlaceList)
        expectAllPlace = set([startPlace, endPlace])
        assert fetchedAllPlace == expectAllPlace

        # assert schedule
        fetchedScheduleList = mockScheduleCRUD.read_all(userEmail=email)
        fetchedScheduleRow = fetchedScheduleList[0]
        fetchedScheduleDict = fetchedScheduleRow._mapping
        fetchedID = fetchedScheduleDict["id"]
        expectScheduleDict = schedule.toRowDict(id=fetchedID)
        assert fetchedScheduleDict == expectScheduleDict

    # delete schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)


def test_schedule_delete(
    mockUserCRUD,
    mockScheduleCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule = Schedule.mock()
        startPlace = Place.mock(id="mockStartPlace")
        endPlace = Place.mock(id="mockEndPlace")
        schedule.startPlaceID = startPlace.id
        schedule.endPlaceID = endPlace.id
        mockScheduleCRUD.create(
            userEmail=email,
            schedule=schedule,
            startPlace=startPlace,
            endPlace=endPlace,
        )

        # when, then
        fetchedScheduleList = mockScheduleCRUD.read_all(userEmail=email)
        fetchedScheduleRow = fetchedScheduleList[0]
        fetchedScheduleDict = fetchedScheduleRow._mapping
        fetchedID = fetchedScheduleDict["id"]

        assert len(fetchedScheduleList) == 1

        mockScheduleCRUD.delete(userEmail=email, scheduleID=fetchedID)

        fetchedScheduleList = mockScheduleCRUD.read_all(userEmail=email)
        assert len(fetchedScheduleList) == 0

    # delete schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
