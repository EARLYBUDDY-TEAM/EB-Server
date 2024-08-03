from eb_fast_api.database.sources.models import User, Schedule, Place


def test_user_create(mockDB):
    email = "email"
    user = User.mock(email = email)
    userCount1 = mockDB.session.query(User).count()

    mockDB.userCreate(user=user)

    fetchedUser = mockDB.userRead(email=email)
    assert user == fetchedUser
    userCount2 = mockDB.session.query(User).count()
    assert userCount2 - userCount1 == 1


def test_user_read(mockDB):
    email = "email"
    user = User.mock(email = email)

    mockDB.userCreate(user=user)
    fetchedUser = mockDB.userRead(email=email)

    assert user == fetchedUser


def test_schedule_create(mockDB):
    email = "email"
    user = User.mock(email = email)
    mockDB.userCreate(user=user)
    schedule = Schedule.mock()
    startPlace = Place.mock(id = 'mockStartPlace')
    endPlace = Place.mock(id = 'mockEndPlace')
    schedule.startPlaceID = startPlace.id
    schedule.endPlaceID = endPlace.id

    mockDB.scheduleCreate(
        userEmail=email,
        schedule=schedule,
        startPlace = startPlace,
        endPlace = endPlace,
    )

    placeCount = mockDB.session.query(Place).count()
    assert placeCount == 2
    fetchedUser = mockDB.userRead(email=email)
    assert len(fetchedUser.schedules) == 1
    assert schedule in fetchedUser.schedules


def test_place_create(mockDB):
    place = Place.mock()

    mockDB.placeCreate(place=place)

    fetchedPlace = mockDB.placeRead(placeID=place.id)
    assert place == fetchedPlace


def test_place_read(mockDB):
    place = Place.mock()

    mockDB.placeCreate(place = place)

    fetchedPlace = mockDB.placeRead(placeID = place.id)
    assert place == fetchedPlace


def test_place_create_check_duplicate(mockDB):
    place1 = Place.mock()
    place2 = Place.mock()
    place3 = Place.mock()

    mockDB.placeCreate(place = place1)
    mockDB.placeCreate(place = place2)
    mockDB.placeCreate(place = place3)

    placeCount = mockDB.session.query(Place).count()
    assert placeCount == 1