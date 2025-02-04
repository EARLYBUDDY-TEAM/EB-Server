from eb_fast_api.database.sources.model.models import User, Schedule, Path
from sqlalchemy import inspect
from eb_fast_api.database.testings.mock_connection import def_create_mock_engine


def test_user_update_one_user(
    mockUser,
    mockUserCRUD,
):
    # given
    newHashedPassword = "NEW" + mockUser.hashedPassword
    newRefreshToken = "NEW" + mockUser.refreshToken
    newFcmToken = "NEW" + mockUser.fcm_token
    new_is_notify = False

    # when

    mockUserCRUD.update(
        key_email=mockUser.email,
        hashedPassword=newHashedPassword,
        refreshToken=newRefreshToken,
        fcm_token=newFcmToken,
        is_notify=new_is_notify,
    )

    # then
    fetched_user_dict = mockUserCRUD.read(email=mockUser.email)

    assert fetched_user_dict["hashedPassword"] == newHashedPassword
    assert fetched_user_dict["refreshToken"] == newRefreshToken
    assert fetched_user_dict["fcm_token"] == newFcmToken
    assert fetched_user_dict["is_notify"] == new_is_notify


def test_user_read_and_create(
    mockUserCRUD,
    mockEngine,
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
        scheduleTableName = Schedule.getTableName(email=first_user.email)
        assert True == inspect(mockEngine).has_table(table_name=scheduleTableName)
        routeTableName = Path.getTableName(email=first_user.email)
        assert True == inspect(mockEngine).has_table(table_name=routeTableName)

    # delete schedule, path table
    finally:
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )


def test_user_update_two_user(
    mockUserCRUD,
    mockEngine,
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
            .filter(User.fcm_token == first_user.fcm_token)
            .count()
        )
        assert user_own_fcm_token_count == 1

        fetched_user_dict = mockUserCRUD.read(email=first_user.email)
        assert fetched_user_dict["hashedPassword"] == newHashedPassword
        assert fetched_user_dict["refreshToken"] == newRefreshToken
        assert fetched_user_dict["fcm_token"] == newFcmToken

    # delete schedule, path table
    finally:
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )


def test_user_get_all_user(
    mockUserCRUD,
    mockEngine,
):
    try:
        # given
        first_email = "first_email"
        second_email = "second_email"
        first_user = User.mock(email=first_email)
        second_user = User.mock(email=second_email)
        mockUserCRUD.create(user=second_user)
        mockUserCRUD.create(user=first_user)

        # when, then
        fetched_user_dict_list = mockUserCRUD.read_all()
        fetched_email_set = set(
            [user_dict["email"] for user_dict in fetched_user_dict_list]
        )
        expect_result = set([first_email, second_email])
        assert expect_result & fetched_email_set == expect_result

    # delete schedule, path table
    finally:
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=first_user.email,
        )
        Schedule.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )
        Path.dropTable(
            engine=def_create_mock_engine(),
            user_email=second_user.email,
        )


def test_user_delete(
    mockUser,
    mockUserCRUD,
    mockSession,
    mockEngine,
):
    # given
    userCount1 = mockSession.query(User).count()
    scheduleTableName = Schedule.getTableName(email=mockUser.email)
    assert True == inspect(mockEngine).has_table(table_name=scheduleTableName)
    pathTableName = Path.getTableName(email=mockUser.email)
    assert True == inspect(mockEngine).has_table(table_name=pathTableName)

    # when
    mockUserCRUD.delete(
        email=mockUser.email,
        def_create_engine=def_create_mock_engine,
    )

    # then
    userCount0 = mockSession.query(User).count()
    assert userCount1 - userCount0 == 1

    assert False == inspect(mockEngine).has_table(table_name=scheduleTableName)
    assert False == inspect(mockEngine).has_table(table_name=pathTableName)
