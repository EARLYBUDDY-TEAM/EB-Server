import httpx, pytest
from unittest.mock import patch

from eb_fast_api.domain.realtime.sources import realtime_feature
from eb_fast_api.domain.realtime.testings import mock_realtime_info
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfo


@pytest.mark.asyncio
async def test_get_bus_station_realtime_info():
    # given
    status_code = 200
    json = {"test": "test"}
    with patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.AsyncClient.get"
    ) as fake_get:
        fake_get.return_value = httpx.Response(
            status_code,
            json=json,
            request=httpx.Request("GET", "test_url"),
        )
        fake_get.start()

        # when
        response = await realtime_feature.get_bus_station_realtime_info(
            station_id=0,
        )

        # then
        assert response.status_code == status_code
        assert response.json() == json


def test_real_time_json_to_real_time_info():
    # given
    mock_json = mock_realtime_info.mock_real_time_json_to_real_time_info_dict

    # when
    decoded = realtime_feature.real_time_json_to_real_time_info(json=mock_json)

    # then
    assert mock_realtime_info.expected_real_time_info == decoded


def test_decode_real_time_info_list():
    # given
    mock_json = mock_realtime_info.mock_decode_real_time_info_list_dict

    # when
    decoded = realtime_feature.decode_real_time_info_list(json=mock_json)

    # then
    expected = [mock_realtime_info.expected_real_time_info] * 5
    assert expected == decoded
