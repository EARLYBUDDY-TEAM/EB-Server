from eb_fast_api.database.sources.models import User, Schedule
from eb_fast_api.database.sources import db_crud
from datetime import datetime


def test_user_create(mockSession):
    email = 'email'
    mockUser = User(email = email, password = 'password')
    userCount1 = mockSession.query(User).count()
    fetchedUser: User

    db_crud.user_create(user = mockUser, session = mockSession)
    fetchedUser = db_crud.user_read(email = email, session = mockSession)

    assert mockUser == fetchedUser
    userCount2 = mockSession.query(User).count()
    assert userCount2 - userCount1 == 1


def test_user_read(mockSession):
    email = 'email'
    mockUser = User(email = email, password = 'password')

    db_crud.user_create(user = mockUser, session = mockSession)
    fetchedUser = db_crud.user_read(email = email, session = mockSession)
    
    assert mockUser == fetchedUser


def test_schedule_create(mockSession):
    email = 'email'
    mockUser = User(email = email, password = 'password')
    db_crud.user_create(user = mockUser, session = mockSession)
    mockSchedule = Schedule(
        id=10,
        title="title",
        time=datetime.now(),
        isNotify=False,
    )

    db_crud.schedule_create(
        userEmail=email,
        schedule=mockSchedule,
        session=mockSession,
    )

    fetchedUser = db_crud.user_read(email = email, session = mockSession)
    assert len(fetchedUser.schedules) == 1
    assert mockSchedule in fetchedUser.schedules