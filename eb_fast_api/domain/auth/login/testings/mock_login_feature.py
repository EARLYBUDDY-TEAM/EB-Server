from unittest.mock import patch
from eb_fast_api.domain.auth.login.sources import login_feature
from eb_fast_api.database.sources.crud.user_crud import UserCRUD
from eb_fast_api.domain.schema.sources.login_info import LoginInfo
from eb_fast_api.domain.schema.sources.schemas import TokenInfo


def patch_check_password_SUCCESS():
    mock_user = dict()
    patch.object(
        login_feature,
        "check_password",
        return_value=mock_user,
    ).start()


def patch_check_password_FAIL():
    def raise_exception(
        user_crud: UserCRUD,
        login_info: LoginInfo,
    ):
        raise Exception("유저정보가 없습니다.")

    patch.object(
        login_feature,
        "check_password",
        new=raise_exception,
    ).start()


def patch_create_auth_token_SUCCESS():
    mock_token_info = TokenInfo.mock()
    patch.object(
        login_feature,
        "create_auth_token",
        return_value=mock_token_info,
    ).start()


def patch_update_tokens_FAIL():
    def raise_exception(
        user_crud: UserCRUD,
        token_info: TokenInfo,
        login_info: LoginInfo,
    ):
        raise Exception("토큰 업데이트에 실패했습니다.")

    patch.object(
        login_feature,
        "update_tokens",
        new=raise_exception,
    ).start()
