from unittest.mock import patch
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as bas


def patcher_get_bus_station_realtime_info(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        bas,
        "get_bus_station_realtime_info",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher


def patcher_decode_realtime_info_list(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        bas,
        "decode_realtime_info_list",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher


def patcher_request(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        bas,
        "request",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher
