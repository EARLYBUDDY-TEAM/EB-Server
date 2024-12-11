from unittest.mock import patch
from eb_fast_api.domain.auth.sources.auth_feature import delete_user_feature


def patcher_delete_user_data_in_db(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        delete_user_feature,
        "delete_user_data_in_db",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher
