from eb_fast_api.database.sources.models import User, Schedule, Place
from eb_fast_api.database.sources import db_crud
from datetime import datetime


def test_user_create(mockSession):
    email = "email"
    mockUser = User.mock(email = email)
    userCount1 = mockSession.query(User).count()
    fetchedUser: User

    db_crud.user_create(user=mockUser, session=mockSession)
    fetchedUser = db_crud.user_read(email=email, session=mockSession)

    assert mockUser == fetchedUser
    userCount2 = mockSession.query(User).count()
    assert userCount2 - userCount1 == 1


def test_user_read(mockSession):
    email = "email"
    mockUser = User.mock(email = email)

    db_crud.user_create(user=mockUser, session=mockSession)
    fetchedUser = db_crud.user_read(email=email, session=mockSession)

    assert mockUser == fetchedUser


def test_schedule_create(mockSession):
    email = "email"
    mockUser = User.mock(email = email)
    db_crud.user_create(user=mockUser, session=mockSession)
    mockSchedule = Schedule.mock()
    mockStartPlace = Place.mock(id = 'mockStartPlace')
    mockEndPlace = Place.mock(id = 'mockEndPlace')
    mockSchedule.startPlaceID = mockStartPlace.id
    mockSchedule.endPlaceID = mockEndPlace.id

    db_crud.schedule_create(
        userEmail=email,
        schedule=mockSchedule,
        startPlace = mockStartPlace,
        endPlace = mockEndPlace,
        session=mockSession,
    )

    placeCount = mockSession.query(Place).count()
    assert placeCount == 2
    fetchedUser = db_crud.user_read(email=email, session=mockSession)
    assert len(fetchedUser.schedules) == 1
    assert mockSchedule in fetchedUser.schedules


def test_place_create(mockSession):
    mockPlace = Place.mock()

    db_crud.place_create(
        place=mockPlace,
        session=mockSession,
    )

    fetchedPlace = db_crud.place_read(
        placeID=mockPlace.id,
        session=mockSession,
    )
    assert mockPlace == fetchedPlace


def test_place_read(mockSession):
    mockPlace = Place.mock()

    db_crud.place_create(place = mockPlace, session = mockSession)
    fetchedPlace = db_crud.place_read(placeID = mockPlace.id, session = mockSession)

    assert mockPlace == fetchedPlace


def test_place_create_check_duplicate(mockSession):
    mockPlace1 = Place.mock()
    mockPlace2 = Place.mock()
    mockPlace3 = Place.mock()

    db_crud.place_create(place = mockPlace1, session = mockSession)
    db_crud.place_create(place = mockPlace2, session = mockSession)
    db_crud.place_create(place = mockPlace3, session = mockSession)

    placeCount = mockSession.query(Place).count()
    assert placeCount == 1
