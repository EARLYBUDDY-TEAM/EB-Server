from eb_fast_api.main import app
from fastapi.testclient import TestClient
from eb_fast_api.domain.realtime.testings.mock_realtime_feature import (
    mock_decode_real_time_info_list_FAIL,
    mock_decode_real_time_info_list_SUCCESS,
    mock_get_bus_station_realtime_info_FAIL,
    mock_get_bus_station_realtime_info_SUCCESS,
    mock_search_subway_schedule_FAIL,
    mock_search_subway_schedule_SUCCESS,
    mock_subway_schedule_json_to_schema_FAIL,
)


def test_get_bus_realtime_info_FAIL_500():
    mock_get_bus_station_realtime_info_FAIL()

    testClient = TestClient(app)
    params = {"station_id": 0}

    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    assert response.status_code == 500


def test_get_bus_realtime_info_FAIL_501():
    mock_get_bus_station_realtime_info_SUCCESS()
    mock_decode_real_time_info_list_FAIL()

    testClient = TestClient(app)
    params = {"station_id": 0}

    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    assert response.status_code == 501


def test_get_subway_schedule_FAIL_500():
    # given
    mock_search_subway_schedule_FAIL()
    testClient = TestClient(app)
    params = {"station_id": 0, "way_code": 1}

    # when
    response = testClient.get(
        "/realtime/get_total_subway_schedule",
        params=params,
    )

    # then
    assert response.status_code == 500


def test_get_subway_schedule_FAIL_501():
    # given
    mock_search_subway_schedule_SUCCESS()
    mock_subway_schedule_json_to_schema_FAIL()
    testClient = TestClient(app)
    params = {"station_id": 0, "way_code": 1}

    # when
    response = testClient.get(
        "/realtime/get_total_subway_schedule",
        params=params,
    )

    # then
    assert response.status_code == 501
