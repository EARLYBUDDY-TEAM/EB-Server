from eb_fast_api.database.sources.model.models import User, Schedule
from sqlalchemy import inspect


def test_create(mockUserCRUD, mockScheduleCRUD, mockSession):
    # given
    email = "email"
    user = User.mock(email=email)
    userCount0 = mockSession.query(User).count()

    # when
    mockUserCRUD.create(user=user)

    # then
    fetchedUser = mockUserCRUD.read(email=email)
    assert user == fetchedUser

    userCount1 = mockSession.query(User).count()
    assert userCount1 - userCount0 == 1

    mockEngine = mockSession.get_bind()
    scheduleTableName = Schedule.getTableName(email=user.email)
    assert True == inspect(mockEngine).has_table(table_name=scheduleTableName)

    # delete schedule table
    mockScheduleCRUD.dropTable(userEmail=user.email)


def test_read(mockUserCRUD, mockScheduleCRUD):
    # given
    email = "email"
    user = User.mock(email=email)

    # when
    mockUserCRUD.create(user=user)
    fetchedUser = mockUserCRUD.read(email=email)

    # then
    assert user == fetchedUser

    # delete schedule table
    mockScheduleCRUD.dropTable(userEmail=user.email)


def test_update(mockUserCRUD, mockScheduleCRUD):
    # given
    email = "email"
    user = User.mock(email=email)
    mockUserCRUD.create(user=user)

    # when
    newHashedPassword = "NEW" + user.hashedPassword
    newRefreshToken = "NEW" + user.refreshToken
    mockUserCRUD.update(
        key_email=email,
        hashedPassword=newHashedPassword,
        refreshToken=newRefreshToken,
    )

    # then
    fetchedUser = mockUserCRUD.read(email=user.email)
    assert fetchedUser.hashedPassword == newHashedPassword
    assert fetchedUser.refreshToken == newRefreshToken

    # delete schedule table
    mockScheduleCRUD.dropTable(userEmail=user.email)
