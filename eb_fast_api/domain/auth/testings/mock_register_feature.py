from unittest.mock import patch
from eb_fast_api.domain.auth.sources.auth_feature import register_feature


def patcher_is_exist_user(return_value: bool):
    patcher = patch.object(
        register_feature,
        "is_exist_user",
        return_value=return_value,
    )
    return patcher


def patcher_isValidRegisterInfo(return_value: bool):
    patcher = patch.object(
        register_feature,
        "isValidRegisterInfo",
        return_value=return_value,
    )
    return patcher


def patcher_createUser(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        register_feature,
        "createUser",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher
