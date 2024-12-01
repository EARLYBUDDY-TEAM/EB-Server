from eb_fast_api.domain.schema.sources.schemas import LoginInfo
from eb_fast_api.domain.auth.login.testings import mock_login_feature


def test_login_ERROR_check_password(testClient):
    # given
    mock_login_feature.patch_check_password_FAIL()

    # when
    path = "/auth/login"
    loginInfo = LoginInfo.mock()
    json = loginInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 400


def test_login_ERROR_update_tokens(testClient):
    # given
    mock_login_feature.patch_check_password_SUCCESS()
    mock_login_feature.patch_create_auth_token_SUCCESS()
    mock_login_feature.patch_update_tokens_FAIL()

    # when
    path = "/auth/login"
    loginInfo = LoginInfo.mock()
    json = loginInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 401
