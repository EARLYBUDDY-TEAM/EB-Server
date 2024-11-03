from unittest.mock import patch
from httpx import Response
from typing import List
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfo


def mock_get_bus_station_realtime_info_SUCCESS():
    async def mock_def_get_bus_station_realtime_info_SUCCESS(
        station_id: int,
    ) -> Response:
        return Response(status_code=200)

    patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.get_bus_station_realtime_info",
        new=mock_def_get_bus_station_realtime_info_SUCCESS,
    ).start()


def mock_get_bus_station_realtime_info_FAIL():
    async def mock_def_get_bus_station_realtime_info_SUCCESS(
        station_id: int,
    ) -> Response:
        raise Exception()

    patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.get_bus_station_realtime_info",
        new=mock_def_get_bus_station_realtime_info_SUCCESS,
    ).start()


def mock_decode_real_time_info_list_SUCCESS():
    async def mock_def_decode_real_time_info_list_SUCCESS(
        json: dict,
    ) -> List[RealTimeInfo]:
        return []

    patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.decode_real_time_info_list",
        new=mock_def_decode_real_time_info_list_SUCCESS,
    ).start()


def mock_decode_real_time_info_list_FAIL():
    async def mock_def_decode_real_time_info_list_FAIL(
        json: dict,
    ) -> List[RealTimeInfo]:
        raise Exception()

    patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.decode_real_time_info_list",
        new=mock_def_decode_real_time_info_list_FAIL,
    ).start()
