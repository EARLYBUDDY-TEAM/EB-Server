import httpx, pytest
from unittest.mock import patch
from datetime import datetime, timedelta
from eb_fast_api.domain.realtime.sources.realtime_feature import subway_realtime_feature
from eb_fast_api.domain.realtime.testings.mock_subway_realtime_info import (
    mockSubwayRealtimeJson,
    mockSubwayId,
    mockUpOrdKey1,
    mockUpOrdKey2,
    mockBarvlDt,
    mockRecptnDt,
)
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfo


@pytest.mark.asyncio
async def test_get_seoul_subway_realtime_info():
    # given
    status_code = 200
    json = {"test": "test"}

    with patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.subway_realtime_feature.AsyncClient.get"
    ) as fake_get:
        fake_get.return_value = httpx.Response(
            status_code,
            json=json,
            request=httpx.Request("GET", "test_url"),
        )
        fake_get.start()

        # when
        response = await subway_realtime_feature.get_seoul_subway_realtime_info(
            station_name="서울",
        )

        # then
        assert response.status_code == status_code
        assert response.json() == json


def test_filter_subway_realtime_data():
    # given
    mock_subway_name = subway_realtime_feature.SubwayID[mockSubwayId]
    subway_direction = 0
    diff_seconds = 30
    mock_now = datetime.strptime(mockRecptnDt, "%Y-%m-%d %H:%M:%S") + timedelta(
        seconds=diff_seconds
    )

    # when
    with patch(
        "eb_fast_api.domain.realtime.sources.realtime_feature.subway_realtime_feature.get_date_time_now"
    ) as fake_get_date_time_now:
        fake_get_date_time_now.return_value = mock_now
        result_subway_realtime_info = (
            subway_realtime_feature.filter_subway_realtime_data(
                data=mockSubwayRealtimeJson,
                subway_name=mock_subway_name,
                subway_direction=subway_direction,
            )
        )

        # then
        arrival_sec = int(mockBarvlDt) + diff_seconds
        expect_subway_realtime_info = RealTimeInfo(
            transport_number=mock_subway_name,
            arrival_sec1=arrival_sec,
            left_station1=int(mockUpOrdKey1[2:5]),
            arrival_sec2=arrival_sec,
            left_station2=int(mockUpOrdKey2[2:5]),
        )

        assert expect_subway_realtime_info == result_subway_realtime_info
