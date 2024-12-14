from unittest.mock import patch
from eb_fast_api.service.realtime.sources.service import subway_realtime_service as sas


def patcher_filter_subway_realtime_data(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        sas,
        "filter_subway_realtime_data",
        return_value=return_value,
        side_effect=side_effect,
    )
    return patcher
