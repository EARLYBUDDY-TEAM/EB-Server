from eb_fast_api.database.sources.models import User, Schedule, Place


def test_user_create(mockCRUD):
    email = "email"
    user = User.mock(email = email)
    userCount1 = mockCRUD.session.query(User).count()

    mockCRUD.userCreate(user=user)

    fetchedUser = mockCRUD.userRead(email=email)
    assert user == fetchedUser
    userCount2 = mockCRUD.session.query(User).count()
    assert userCount2 - userCount1 == 1


def test_user_read(mockCRUD):
    email = "email"
    user = User.mock(email = email)

    mockCRUD.userCreate(user=user)
    fetchedUser = mockCRUD.userRead(email=email)

    assert user == fetchedUser


def test_schedule_create(mockCRUD):
    email = "email"
    user = User.mock(email = email)
    mockCRUD.userCreate(user=user)
    schedule = Schedule.mock()
    startPlace = Place.mock(id = 'mockStartPlace')
    endPlace = Place.mock(id = 'mockEndPlace')
    schedule.startPlaceID = startPlace.id
    schedule.endPlaceID = endPlace.id

    mockCRUD.scheduleCreate(
        userEmail=email,
        schedule=schedule,
        startPlace = startPlace,
        endPlace = endPlace,
    )

    placeCount = mockCRUD.session.query(Place).count()
    assert placeCount == 2
    fetchedUser = mockCRUD.userRead(email=email)
    assert len(fetchedUser.schedules) == 1
    assert schedule in fetchedUser.schedules


def test_place_create(mockCRUD):
    place = Place.mock()

    mockCRUD.placeCreate(place=place)

    fetchedPlace = mockCRUD.placeRead(placeID=place.id)
    assert place == fetchedPlace


def test_place_read(mockCRUD):
    place = Place.mock()

    mockCRUD.placeCreate(place = place)

    fetchedPlace = mockCRUD.placeRead(placeID = place.id)
    assert place == fetchedPlace


def test_place_create_check_duplicate(mockCRUD):
    place1 = Place.mock()
    place2 = Place.mock()
    place3 = Place.mock()

    mockCRUD.placeCreate(place = place1)
    mockCRUD.placeCreate(place = place2)
    mockCRUD.placeCreate(place = place3)

    placeCount = mockCRUD.session.query(Place).count()
    assert placeCount == 1