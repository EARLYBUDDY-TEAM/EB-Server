from unittest.mock import patch
from eb_fast_api.database.sources.crud.cruds import PathCRUD


def patcher_read(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        PathCRUD,
        "read",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
