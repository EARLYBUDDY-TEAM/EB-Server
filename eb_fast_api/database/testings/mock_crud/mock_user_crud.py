from unittest.mock import patch
from typing import Optional, List, Callable
from eb_fast_api.database.sources.model.user import User
from eb_fast_api.database.sources.crud.user_crud import UserCRUD


mock_user_dict = User.mock().to_dict()


def patcher_delete_SUCCESS():
    patcher = patch.object(
        UserCRUD,
        "delete",
        return_value=None,
    )

    return patcher


def patcher_delete_FAIL():
    patcher = patch.object(
        UserCRUD,
        "delete",
        side_effect=Exception("mock delete FAIL"),
    )

    return patcher


def patcher_update():
    patcher = patch.object(
        UserCRUD,
        "update",
        return_value=None,
    )

    return patcher


def patch_user_crud_read(return_value: Optional[dict]):
    patcher = patch.object(
        UserCRUD,
        "read",
        return_value=return_value,
    )

    return patcher


def patcher_read_all(return_value: List[dict]) -> List[dict]:
    patcher = patch.object(
        UserCRUD,
        "read_all",
        return_value=return_value,
    )

    return patcher
