from eb_fast_api.database.sources.model.models import User, Schedule, Path
from sqlalchemy import inspect


def test_user_read_and_create(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
    mockSession,
):
    try:
        # given
        first_email = "first_email"
        second_email = "second_email"
        first_user = User.mock(email=first_email)
        second_user = User.mock(email=second_email)
        userCount0 = mockSession.query(User).count()

        # when
        mockUserCRUD.create(user=first_user)
        mockUserCRUD.create(user=second_user)

        # then
        fetched_user_dict = mockUserCRUD.read(email=first_email)
        expect_user_dict = first_user.to_dict()
        assert expect_user_dict == fetched_user_dict

        userCount2 = mockSession.query(User).count()
        assert userCount2 - userCount0 == 2

        user_own_fcm_token_count = (
            mockSession.query(User)
            .filter(User.fcm_token == second_user.fcm_token)
            .count()
        )
        assert user_own_fcm_token_count == 1

        # assert dict check..

        mockEngine = mockSession.get_bind()
        scheduleTableName = Schedule.getTableName(email=first_user.email)
        assert True == inspect(mockEngine).has_table(table_name=scheduleTableName)
        routeTableName = Path.getTableName(email=first_user.email)
        assert True == inspect(mockEngine).has_table(table_name=routeTableName)

    # delete schedule, path table
    finally:
        mockScheduleCRUD.dropTable(userEmail=first_user.email)
        mockPathCRUD.dropTable(user_email=first_user.email)
        mockScheduleCRUD.dropTable(userEmail=second_user.email)
        mockPathCRUD.dropTable(user_email=second_user.email)


def test_user_update_two_user(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
    mockSession,
):
    try:
        # given
        first_email = "first_email"
        first_user = User.mock(email=first_email)
        second_email = "second_email"
        second_user = User.mock(email=second_email)
        mockUserCRUD.create(user=second_user)
        mockUserCRUD.create(user=first_user)

        # when
        newHashedPassword = "NEW" + first_user.hashedPassword
        newRefreshToken = "NEW" + first_user.refreshToken
        newFcmToken = "NEW" + first_user.fcm_token
        mockUserCRUD.update(
            key_email=first_email,
            hashedPassword=newHashedPassword,
            refreshToken=newRefreshToken,
            fcm_token=newFcmToken,
        )

        # then
        user_own_fcm_token_count = (
            mockSession.query(User)
            .filter(User.fcm_token == second_user.fcm_token)
            .count()
        )
        assert user_own_fcm_token_count == 1

        fetched_user_dict = mockUserCRUD.read(email=first_user.email)
        assert fetched_user_dict["hashedPassword"] == newHashedPassword
        assert fetched_user_dict["refreshToken"] == newRefreshToken
        assert fetched_user_dict["fcm_token"] == newFcmToken

    # delete schedule, path table
    finally:
        mockScheduleCRUD.dropTable(userEmail=first_user.email)
        mockPathCRUD.dropTable(user_email=first_user.email)
        mockScheduleCRUD.dropTable(userEmail=second_user.email)
        mockPathCRUD.dropTable(user_email=second_user.email)


def test_user_update_one_user(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
    mockSession,
):
    try:
        # given
        first_email = "first_email"
        first_user = User.mock(email=first_email)
        mockUserCRUD.create(user=first_user)

        # when
        newHashedPassword = "NEW" + first_user.hashedPassword
        newRefreshToken = "NEW" + first_user.refreshToken
        newFcmToken = "NEW" + first_user.fcm_token
        mockUserCRUD.update(
            key_email=first_email,
            hashedPassword=newHashedPassword,
            refreshToken=newRefreshToken,
            fcm_token=newFcmToken,
        )

        # then
        fetched_user_dict = mockUserCRUD.read(email=first_user.email)
        assert fetched_user_dict["hashedPassword"] == newHashedPassword
        assert fetched_user_dict["refreshToken"] == newRefreshToken
        assert fetched_user_dict["fcm_token"] == newFcmToken

    # delete schedule, path table
    finally:
        mockScheduleCRUD.dropTable(userEmail=first_user.email)
        mockPathCRUD.dropTable(user_email=first_user.email)