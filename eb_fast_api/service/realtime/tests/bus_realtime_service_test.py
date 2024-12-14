import httpx, pytest
from unittest.mock import patch

from eb_fast_api.service.realtime.sources import bus_realtime_service as bas
from eb_fast_api.service.realtime.testings import mock_bus_realtime_info as mai


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
