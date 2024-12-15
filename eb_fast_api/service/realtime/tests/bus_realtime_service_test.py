import httpx, pytest
from unittest.mock import patch

from eb_fast_api.service.realtime.sources.service import bus_realtime_service as brs
from eb_fast_api.service.realtime.testings import mock_bus_realtime_info as mbri
from eb_fast_api.service.realtime.testings import mock_bus_realtime_service as mbrs
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
        brs.AsyncClient,
        "get",
        return_value=fake_get_return_value,
    ) as fake_get:
        # when
        response = await brs.get_bus_station_realtime_info(
            station_id=0,
        )

        # then
        assert response.status_code == status_code
        assert response.json() == json


def test_arrival_json_to_arrival_info():
    # given
    json = mbri.mock_bus_arrival_json

    # when
    decoded = brs.arrival_json_to_arrival_info(json=json)

    # then
    assert mbri.expected_arrival_info1 == decoded


def test_realtime_json_to_realtime_info():
    # given
    json = mbri.mock_bus_realtime_json

    # when
    decoded = brs.realtime_json_to_realtime_info(json=json)

    # then
    assert mbri.expected_realtime_info == decoded


def test_decode_realtime_info_list_SORT():
    # given
    json = mbri.mock_bus_decode_realtime_info_list_dict()
    real = json["result"]["real"]
    expect_arrival_info = real[len(real) - 1]["arrival1"]["arrivalSec"]

    # when
    decoded = brs.decode_realtime_info_list(json=json)

    # then
    # last index -> first index
    assert expect_arrival_info == decoded[0].arrival_info1.arrival_sec


@pytest.mark.asyncio
async def test_request_FAIL_GetBusStationRealtimeInfoError():
    # given
    pather = mbrs.patcher_get_bus_station_realtime_info(side_effect=Exception())
    pather.start()
    station_id = 0

    # when, then
    try:
        response = await brs.request(station_id=station_id)
        assert False
    except Exception as e:
        assert True

    # teardown
    finally:
        pather.stop()


@pytest.mark.asyncio
async def test_request_SUCCESS():
    # given
    fake_response = httpx.Response(
        200,
        json={"test": "test"},
        request=httpx.Request("GET", "testURL"),
    )
    mock_realtime_info_list = [RealTimeInfo.mock()]
    patcher_get_bus_station_realtime_info = mbrs.patcher_get_bus_station_realtime_info(
        return_value=fake_response
    )
    patcher_decode_realtime_info_list = mbrs.patcher_decode_realtime_info_list(
        return_value=mock_realtime_info_list
    )

    patcher_get_bus_station_realtime_info.start()
    patcher_decode_realtime_info_list.start()
    station_id = 0

    # when, then
    try:
        realtime_info_list = await brs.request(station_id=station_id)
        assert realtime_info_list == mock_realtime_info_list
    except Exception as e:
        assert False

    # teardown
    finally:
        patcher_get_bus_station_realtime_info.stop()
        patcher_decode_realtime_info_list.stop()
