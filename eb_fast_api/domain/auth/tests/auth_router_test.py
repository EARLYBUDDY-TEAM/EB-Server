from eb_fast_api.domain.schema.sources.schemas import RegisterInfo, LoginInfo
from eb_fast_api.domain.auth.sources.auth_schema import ChangePasswordInfo
from eb_fast_api.domain.auth.testings import (
    mock_login_feature,
    mock_register_feature,
    mock_change_password_feature,
)
from eb_fast_api.database.testings.mock_crud import mock_user_crud


def test_login_ERROR_check_password(testClient):
    # given
    patcher = mock_login_feature.patch_check_password_FAIL()
    patcher.start()

    # when
    path = "/auth/login"
    loginInfo = LoginInfo.mock()
    json = loginInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 400
    patcher.stop()


def test_login_ERROR_update_tokens(testClient):
    # given
    patcher_check_password = mock_login_feature.patch_check_password_SUCCESS()
    patcher_create_auth_token = mock_login_feature.patch_create_auth_token_SUCCESS()
    patcher_update_tokens = mock_login_feature.patch_update_tokens_FAIL()
    patcher_check_password.start()
    patcher_create_auth_token.start()
    patcher_update_tokens.start()

    # when
    path = "/auth/login"
    loginInfo = LoginInfo.mock()
    json = loginInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 401
    patcher_check_password.stop()
    patcher_create_auth_token.stop()
    patcher_update_tokens.stop()


def test_register_FAIL_invalid_register_info(testClient):
    # given
    patcher = mock_register_feature.patch_isValidRegisterInfo(False)
    patcher.start()

    # when
    path = "/auth/register"
    registerInfo = RegisterInfo.mock()
    json = registerInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 400
    patcher.stop()


def test_register_FAIL_createUser(testClient):
    # given
    patcher_isValidRegisterInfo = mock_register_feature.patch_isValidRegisterInfo(True)
    patcher_createUser = mock_register_feature.patch_createUser_FAIL()
    patcher_isValidRegisterInfo.start()
    patcher_createUser.start()

    # when
    path = "/auth/register"
    registerInfo = RegisterInfo.mock()
    json = registerInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 401
    patcher_isValidRegisterInfo.stop()
    patcher_createUser.stop()


def test_change_password_FAIL_status_code_400(testClient):
    # given
    patcher_isValidPassword = mock_change_password_feature.patcher_isValidPassword(
        return_value=False
    )
    patcher_isValidPassword.start()

    # when
    path = "/auth/change_password"
    changePasswordInfo = ChangePasswordInfo.mock()
    json = changePasswordInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 400
    patcher_isValidPassword.stop()


def test_change_password_FAIL_status_code_401(testClient):
    # given
    patcher_isValidPassword = mock_change_password_feature.patcher_isValidPassword(
        return_value=True
    )
    patcher_update_pwd = mock_change_password_feature.patcher_update_pwd_FAIL()
    patcher_isValidPassword.start()
    patcher_update_pwd.start()

    # when
    path = "/auth/change_password"
    changePasswordInfo = ChangePasswordInfo.mock()
    json = changePasswordInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 401
    patcher_isValidPassword.stop()
    patcher_update_pwd.stop()


def test_change_password_SUCCESS(testClient):
    # given
    patcher_isValidPassword = mock_change_password_feature.patcher_isValidPassword(
        return_value=True
    )
    patcher_update_pwd = mock_change_password_feature.patcher_update_pwd_SUCCESS()
    patcher_isValidPassword.start()
    patcher_update_pwd.start()

    # when
    path = "/auth/change_password"
    changePasswordInfo = ChangePasswordInfo.mock()
    json = changePasswordInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 200
    patcher_isValidPassword.stop()
    patcher_update_pwd.stop()


def test_remove_user_SUCCESS(testClient):
    # given
    patcher_delete = mock_user_crud.patcher_delete_SUCCESS()
    patcher_delete.start()

    # when
    path = "/auth/remove_user"
    headers = {"access_token": "access_token"}
    response = testClient.post(
        path,
        headers=headers,
    )

    # then
    assert response.status_code == 200
    patcher_delete.stop()


def test_remove_user_FAIL_delete(testClient):
    # given
    patcher_delete = mock_user_crud.patcher_delete_FAIL()
    patcher_delete.start()

    # when
    path = "/auth/remove_user"
    headers = {"access_token": "access_token"}
    response = testClient.post(
        path,
        headers=headers,
    )

    # then
    assert response.status_code == 400
    patcher_delete.stop()
