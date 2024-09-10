from eb_fast_api.database.sources.model.models import User, Schedule, Place


def test_userCreate(mockUserCRUD):
    email = "email"
    user = User.mock(email=email)
    userCount1 = mockUserCRUD.session.query(User).count()

    mockUserCRUD.create(user=user)

    fetchedUser = mockUserCRUD.read(email=email)
    assert user == fetchedUser
    userCount2 = mockUserCRUD.session.query(User).count()
    assert userCount2 - userCount1 == 1


def test_userRead(mockUserCRUD):
    email = "email"
    user = User.mock(email=email)

    mockUserCRUD.create(user=user)
    fetchedUser = mockUserCRUD.read(email=email)

    assert user == fetchedUser


def test_scheduleCreate(mockUserCRUD, mockScheduleCRUD):
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

    placeCount = mockScheduleCRUD.session.query(Place).count()
    assert placeCount == 2
    fetchedUser = mockUserCRUD.read(email=email)
    assert len(fetchedUser.schedules) == 1
    assert schedule in fetchedUser.schedules


def test_placeCreate(mockPlaceCRUD):
    place = Place.mock()

    mockPlaceCRUD.create(place=place)

    fetchedPlace = mockPlaceCRUD.read(placeID=place.id)
    assert place == fetchedPlace


def test_placeRead(mockPlaceCRUD):
    place = Place.mock()

    mockPlaceCRUD.create(place=place)

    fetchedPlace = mockPlaceCRUD.read(placeID=place.id)
    assert place == fetchedPlace


def test_placeCreate_check_duplicate(mockPlaceCRUD):
    place1 = Place.mock()
    place2 = Place.mock()
    place3 = Place.mock()

    mockPlaceCRUD.create(place=place1)
    mockPlaceCRUD.create(place=place2)
    mockPlaceCRUD.create(place=place3)

    placeCount = mockPlaceCRUD.session.query(Place).count()
    assert placeCount == 1
