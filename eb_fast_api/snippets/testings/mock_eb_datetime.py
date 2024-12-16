from unittest.mock import patch
from datetime import datetime, timedelta
from eb_fast_api.snippets.sources import eb_datetime


datetime_str = "2024-07-28T05:04:32.299Z"
tmp_datetime = datetime.fromisoformat(datetime_str)
mock_now = tmp_datetime.replace(microsecond=0, tzinfo=None)


def patcher_get_datetime_now(
    return_value: datetime = mock_now,
):
    def mock_get_datetime_now():
        return return_value.replace(
            tzinfo=None,
            microsecond=0,
        )

    pather = patch.object(
        eb_datetime,
        "get_datetime_now",
        mock_get_datetime_now,
    )
    return pather
