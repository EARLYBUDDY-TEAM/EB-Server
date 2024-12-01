from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.database.testings.mock_crud.mock_user_crud import (
    patch_user_crud_read_SUCCESS,
    patch_user_crud_read_FAIL,
    mock_user_dict,
)
from eb_fast_api.domain.schema.sources.login_info import LoginInfo
from eb_fast_api.domain.schema.sources.token_info import TokenInfo
from eb_fast_api.snippets.testings.mock_pwdcrypt import (
    patch_pwdcrypt_check_SUCCESS,
    patch_pwdcrypt_check_FAIL,
)
from eb_fast_api.service.jwt.testings.mock_jwt_service import (
    patcher_create_access_token,
    patcher_create_refresh_token,
    mock_token,
)
from eb_fast_api.service.jwt.sources.jwt_service import jwtService
from eb_fast_api.database.sources.model.models import User


def test_check_password_FAIL_No_User(loginMockUserCRUD):
    # given
    patcher = patch_user_crud_read_FAIL()
    patcher.start()
    mock_login_info = LoginInfo.mock()

    # when, then
    try:
        login_feature.check_password(
            user_crud=loginMockUserCRUD,
            login_info=mock_login_info,
        )
    except Exception as e:
        assert e.args[0] == "유저정보가 없습니다."
    finally:
        patcher.stop()


def test_check_password_FAIL_Wrong_Password(loginMockUserCRUD):
    # given
    patcher_user_crud = patch_user_crud_read_SUCCESS()
    patcher_user_crud.start()
    patcher_pwdcrypt = patch_pwdcrypt_check_FAIL()
    patcher_pwdcrypt.start()
    mock_login_info = LoginInfo.mock()

    # when, then
    try:
        login_feature.check_password(
            user_crud=loginMockUserCRUD,
            login_info=mock_login_info,
        )
    except Exception as e:
        assert e.args[0] == "잘못된 패스워드 입니다."
    finally:
        patcher_user_crud.stop()
        patcher_pwdcrypt.stop()


def test_check_password_SUCCESS(loginMockUserCRUD):
    # given
    patcher_user_crud = patch_user_crud_read_SUCCESS()
    patcher_user_crud.start()
    patcher_pwdcrypt = patch_pwdcrypt_check_SUCCESS()
    patcher_pwdcrypt.start()
    mock_login_info = LoginInfo.mock()

    # when, then
    try:
        expect_user = login_feature.check_password(
            user_crud=loginMockUserCRUD,
            login_info=mock_login_info,
        )
        assert expect_user == mock_user_dict
    except Exception as e:
        assert False
    finally:
        patcher_user_crud.stop()
        patcher_pwdcrypt.stop()


def test_create_auth_token():
    # given
    patcher_access = patcher_create_access_token()
    patcher_refresh = patcher_create_refresh_token()
    patcher_access.start()
    patcher_refresh.start()

    # when
    token_info = login_feature.create_auth_token(
        user=mock_user_dict,
        jwtService=jwtService,
    )

    # then
    expect_token_info = TokenInfo(
        accessToken=mock_token,
        refreshToken=mock_token,
    )

    try:
        assert token_info == expect_token_info
    finally:
        patcher_access.stop()
        patcher_refresh.stop()
