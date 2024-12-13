from eb_fast_api.service.notification.sources.feature import fcm_feature as ff
from unittest.mock import patch
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.database.sources.database import EBDataBase


def test_get_fcm_token():
    # given
    expected_fcm_token = "expected_fcm_token"
    mock_user_dict = {"fcm_token": expected_fcm_token}

    # when, then
    with patch.object(
        UserCRUD,
        "read",
        return_value=mock_user_dict,
    ):
        user_crud = EBDataBase.user.createCRUD()
        fcm_token = ff.get_fcm_token(
            user_email="",
            user_crud=user_crud,
        )

        assert fcm_token == expected_fcm_token
