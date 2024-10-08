from eb_fast_api.env.sources.env import (
    API_VALUE,
    MYSQL_VALUE,
    TEST_USER_VALUE,
    dot_env_dir,
)


def test_get_value_API():
    env_file = dot_env_dir.joinpath(".api_example")
    env_api = API_VALUE(env_file=env_file)

    assert env_api.kakaomap == "kakaomap"
    assert env_api.odsay == "odsay"


def test_get_value_MYSQL():
    env_file = dot_env_dir.joinpath(".mysql_example")
    env_mysql = MYSQL_VALUE(env_file=env_file)

    assert env_mysql.MYSQL_PORT == 3306
    assert env_mysql.MYSQL_DATABASE == "earlybuddy_db"
    assert env_mysql.MYSQL_USER == "earlybuddy"
    assert env_mysql.MYSQL_PASSWORD == "1234"


def test_get_value_TEST_USER():
    env_file = dot_env_dir.joinpath(".test_user_example")
    env_test_user = TEST_USER_VALUE(env_file=env_file)

    assert env_test_user.nick_name == "nick_name"
    assert env_test_user.email == "email@email.com"
    assert env_test_user.password == "password12"
