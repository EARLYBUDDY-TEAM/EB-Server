from unittest.mock import patch
from eb_fast_api.domain.auth.sources.auth_feature import login_feature
from eb_fast_api.database.sources.crud.user_crud import UserCRUD
from eb_fast_api.domain.schema.sources.login_info import LoginInfo
from eb_fast_api.domain.schema.sources.schemas import TokenInfo


def patch_check_password_SUCCESS():
    mock_user = dict()
    patcher = patch.object(
        login_feature,
        "check_password",
        return_value=mock_user,
    )
    return patcher


def patch_check_password_FAIL():
    patcher = patch.object(
        login_feature,
        "check_password",
        side_effect=Exception("유저정보가 없습니다."),
    )
    return patcher


def patch_create_auth_token_SUCCESS():
    mock_token_info = TokenInfo.mock()
    patcher = patch.object(
        login_feature,
        "create_auth_token",
        return_value=mock_token_info,
    )
    return patcher


def patch_update_tokens_FAIL():
    patcher = patch.object(
        login_feature,
        "update_tokens",
        side_effect=Exception("토큰 업데이트에 실패했습니다."),
    )
    return patcher
