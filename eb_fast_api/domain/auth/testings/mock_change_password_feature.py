from unittest.mock import patch
from eb_fast_api.domain.auth.sources.auth_feature import change_password_feature as cpf


def patcher_isValidPassword(return_value: bool):
    patcher = patch.object(
        cpf,
        "isValidPassword",
        return_value=return_value,
    )
    return patcher


def patcher_update_pwd_FAIL():
    patcher = patch.object(
        cpf,
        "update_pwd",
        side_effect=Exception("패스워드 업데이트에 실패했습니다."),
    )
    return patcher


def patcher_update_pwd_SUCCESS():
    patcher = patch.object(
        cpf,
        "update_pwd",
        return_value=None,
    )
    return patcher  
