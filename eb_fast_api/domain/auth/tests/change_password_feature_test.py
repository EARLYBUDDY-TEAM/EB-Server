from eb_fast_api.domain.auth.sources.auth_feature import change_password_feature
from eb_fast_api.database.testings.mock_crud import mock_user_crud as muc


def test_update_pwd(mockUserCRUD):
    # given
    patcher = muc.patcher_update()
    patcher.start()

    # when, then
    try:
        change_password_feature.update_pwd(
            email="test@test.com",
            password="test1234",
            user_crud=mockUserCRUD,
        )
    except Exception as e:
        print(e)
        assert False
    finally:
        patcher.stop()
