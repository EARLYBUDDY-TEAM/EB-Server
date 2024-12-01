from eb_fast_api.domain.schema.sources.schemas import RegisterInfo
from eb_fast_api.domain.auth.register.testings import mock_register_feature


def test_register_FAIL_invalid_register_info(testClient):
    # given
    mock_register_feature.patch_isValidRegisterInfo(False)

    # when
    path = "/auth/register"
    registerInfo = RegisterInfo.mock()
    json = registerInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 400


def test_register_FAIL_createUser(testClient):
    # given
    mock_register_feature.patch_isValidRegisterInfo(True)
    mock_register_feature.patch_createUser_FAIL()

    # when
    path = "/auth/register"
    registerInfo = RegisterInfo.mock()
    json = registerInfo.model_dump(mode="json")
    response = testClient.post(path, json=json)

    # then
    assert response.status_code == 401
