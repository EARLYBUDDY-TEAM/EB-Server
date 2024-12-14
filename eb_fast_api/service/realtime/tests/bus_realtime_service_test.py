import httpx, pytest
from unittest.mock import patch

from eb_fast_api.service.realtime.sources.service import bus_realtime_service as bas
from eb_fast_api.service.realtime.testings import mock_bus_realtime_info as mai
from eb_fast_api.service.realtime.testings import mock_bus_realtime_service as mbrs
from eb_fast_api.service.realtime.sources.error.bus_realtime_error import (
    GetBusStationRealtimeInfoError,
    DecodeRealtimeInfoListError,
)
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo


@pytest.mark.asyncio
async def test_get_bus_station_realtime_info():
    # given
    status_code = 200
    json = {"test": "test"}
    fake_get_return_value = httpx.Response(
        status_code,
        json=json,
        request=httpx.Request("GET", "test_url"),
    )

    with patch.object(
        bas.AsyncClient,
        "get",
        return_value=fake_get_return_value,
    ) as fake_get:
        # when
        response = await bas.get_bus_station_realtime_info(
            station_id=0,
        )

        # then
        assert response.status_code == status_code
        assert response.json() == json


def test_realtime_json_to_realtime_info():
    # given
    mock_json = mai.mock_realtime_json_to_realtime_info_dict

    # when
    decoded = bas.realtime_json_to_realtime_info(json=mock_json)

    # then
    assert mai.expected_realtime_info == decoded


@pytest.mark.asyncio
async def test_request_FAIL_GetBusStationRealtimeInfoError():
    # given
    pather = mbrs.patcher_get_bus_station_realtime_info(side_effect=Exception())
    pather.start()
    station_id = 0

    # when, then
    try:
        response = await bas.request(station_id=station_id)
        assert False
    except Exception as e:
        assert isinstance(e, GetBusStationRealtimeInfoError)

    # teardown
    finally:
        pather.stop()


@pytest.mark.asyncio
async def test_request_FAIL_DecodeRealtimeInfoListError():
    # given
    fake_response = httpx.Response(
        200,
        json={"test": "test"},
        request=httpx.Request("GET", "testURL"),
    )
    patcher_get_bus_station_realtime_info = mbrs.patcher_get_bus_station_realtime_info(
        return_value=fake_response
    )
    patcher_decode_realtime_info_list = mbrs.patcher_decode_realtime_info_list(
        side_effect=Exception()
    )

    patcher_get_bus_station_realtime_info.start()
    patcher_decode_realtime_info_list.start()
    station_id = 0

    # when, then
    try:
        response = await bas.request(station_id=station_id)
        assert False
    except Exception as e:
        assert isinstance(e, DecodeRealtimeInfoListError)

    # teardown
    finally:
        patcher_get_bus_station_realtime_info.stop()
        patcher_decode_realtime_info_list.stop()


@pytest.mark.asyncio
async def test_request_SUCCESS():
    # given
    fake_response = httpx.Response(
        200,
        json={"test": "test"},
        request=httpx.Request("GET", "testURL"),
    )
    mock_realtime_info = RealTimeInfo.mock()
    patcher_get_bus_station_realtime_info = mbrs.patcher_get_bus_station_realtime_info(
        return_value=fake_response
    )
    patcher_decode_realtime_info_list = mbrs.patcher_decode_realtime_info_list(
        return_value=[mock_realtime_info]
    )

    patcher_get_bus_station_realtime_info.start()
    patcher_decode_realtime_info_list.start()
    station_id = 0

    # when, then
    try:
        realtime_info_list = await bas.request(station_id=station_id)
        assert realtime_info_list == [mock_realtime_info]
    except Exception as e:
        assert False

    # teardown
    finally:
        patcher_get_bus_station_realtime_info.stop()
        patcher_decode_realtime_info_list.stop()
