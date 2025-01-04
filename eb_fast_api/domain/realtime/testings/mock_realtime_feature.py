from unittest.mock import patch
from eb_fast_api.domain.realtime.sources import realtime_feature


def patcher_get_bus_station_realtime_json(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        realtime_feature,
        "get_bus_station_realtime_json",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher


def patcher_get_seoul_subway_realtime_json(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        realtime_feature,
        "get_seoul_subway_realtime_json",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
