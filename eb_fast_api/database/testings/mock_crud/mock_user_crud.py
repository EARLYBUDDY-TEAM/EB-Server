from unittest.mock import patch
from typing import Optional
from eb_fast_api.database.sources.model.user import User
from eb_fast_api.database.sources.crud.user_crud import UserCRUD


mock_user_dict = User.mock().to_dict()


def patch_user_crud_read_FAIL():
    def mock_def_user_crud_read_FAIL(
        self,
        email: str,
    ) -> Optional[dict]:
        return None

    patcher = patch(
        "eb_fast_api.database.sources.crud.user_crud.UserCRUD.read",
        new=mock_def_user_crud_read_FAIL,
    )

    return patcher


def patch_user_crud_read_SUCCESS(mock_user: dict = mock_user_dict):
    def mock_def_user_crud_read_SUCCESS(
        self,
        email: str,
    ) -> Optional[dict]:
        return mock_user

    patcher = patch(
        "eb_fast_api.database.sources.crud.user_crud.UserCRUD.read",
        new=mock_def_user_crud_read_SUCCESS,
    )

    return patcher
