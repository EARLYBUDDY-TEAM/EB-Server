from unittest.mock import patch
from eb_fast_api.domain.auth.sources.auth_feature import register_feature


def patch_isValidRegisterInfo(isSuccess: bool):
    patcher = patch.object(
        register_feature,
        "isValidRegisterInfo",
        return_value=isSuccess,
    )
    return patcher


def patch_createUser_FAIL():
    def raiseException():
        raise Exception("이미 존재하는 사용자입니다.")

    patcher = patch.object(
        register_feature,
        "createUser",
        new=raiseException,
    )
    return patcher


def patch_createUser_SUCCESS():
    patcher = patch.object(
        register_feature,
        "createUser",
        return_value=None,
    )
    return patcher
