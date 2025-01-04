from eb_fast_api.domain.schema.sources.schemas import TokenInfo
from eb_fast_api.domain.token.eb_token.testings import mock_eb_token_feature


def test_recreate_token_FAIL_verifyToken(mockTestClient):
    # given
    patcher_verifyToken_FAIL = mock_eb_token_feature.patcher_verifyToken_FAIL()
    patcher_verifyToken_FAIL.start()

    # when
    path = "/token/eb/recreate"
    headers = {"refresh_token": "refreshToken"}
    response = mockTestClient.get(
        path,
        headers=headers,
    )

    # then
    assert response.status_code == 490
    patcher_verifyToken_FAIL.stop()


def test_recreate_token_FAIL_update_refresh_token(mockTestClient):
    # given
    patcher_verifyToken_SUCCESS = mock_eb_token_feature.patcher_verifyToken_SUCCESS(
        email="email",
    )
    tokenInfo = TokenInfo.mock()
    patcher_create_token_info = mock_eb_token_feature.patcher_create_token_info(
        tokenInfo=tokenInfo,
    )
    patcher_update_refresh_token_FAIL = (
        mock_eb_token_feature.patcher_update_refresh_token_FAIL()
    )

    patcher_verifyToken_SUCCESS.start()
    patcher_create_token_info.start()
    patcher_update_refresh_token_FAIL.start()

    # when
    path = "/token/eb/recreate"
    headers = {"refresh_token": "refreshToken"}
    response = mockTestClient.get(
        path,
        headers=headers,
    )

    # then
    assert response.status_code == 491

    patcher_verifyToken_SUCCESS.stop()
    patcher_create_token_info.stop()
    patcher_update_refresh_token_FAIL.stop()
