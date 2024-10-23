from eb_fast_api.database.sources.model.models import User, Schedule, Route
from sqlalchemy import inspect


def test_user_read_and_create(
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
    mockSession,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        userCount0 = mockSession.query(User).count()

        # when
        mockUserCRUD.create(user=user)

        # then
        fetched_user_dict = mockUserCRUD.read(email=email)
        expect_user_dict = user.to_dict()
        assert expect_user_dict == fetched_user_dict

        userCount1 = mockSession.query(User).count()
        assert userCount1 - userCount0 == 1
        # assert dict check..

        mockEngine = mockSession.get_bind()
        scheduleTableName = Schedule.getTableName(email=user.email)
        assert True == inspect(mockEngine).has_table(table_name=scheduleTableName)
        routeTableName = Route.getTableName(email=user.email)
        assert True == inspect(mockEngine).has_table(table_name=routeTableName)

    # delete schedule, route table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockRouteCRUD.dropTable(user_email=user.email)


def test_user_update(
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
):
    try:
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
        fetched_user_dict = mockUserCRUD.read(email=user.email)
        assert fetched_user_dict["hashedPassword"] == newHashedPassword
        assert fetched_user_dict["refreshToken"] == newRefreshToken

    # delete schedule, route table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockRouteCRUD.dropTable(user_email=user.email)
