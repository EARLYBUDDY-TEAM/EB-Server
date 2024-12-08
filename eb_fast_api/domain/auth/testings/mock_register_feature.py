from unittest.mock import patch
from email_validator import validate_email
from eb_fast_api.domain.schema.sources.schemas import RegisterInfo
from eb_fast_api.database.sources.crud.user_crud import UserCRUD
from eb_fast_api.domain.auth.sources.auth_feature import register_feature


def patch_isValidRegisterInfo(isSuccess: bool):
    return patch.object(
        register_feature,
        "isValidRegisterInfo",
        return_value=isSuccess,
    ).start()


def patch_createUser_FAIL():
    def raiseException():
        raise Exception("이미 존재하는 사용자입니다.")

    patch.object(
        register_feature,
        "createUser",
        new=raiseException,
    ).start()


def patch_createUser_SUCCESS():
    patch.object(
        register_feature,
        "createUser",
        return_value=None,
    ).start()
