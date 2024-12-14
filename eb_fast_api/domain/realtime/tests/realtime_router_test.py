from eb_fast_api.main import app
from fastapi.testclient import TestClient
from eb_fast_api.service.realtime.testings import mock_bus_realtime_service as mbrs
from eb_fast_api.service.realtime.testings import mock_subway_realtime_service as msrs
from eb_fast_api.domain.realtime.testings import mock_realtime_feature as mrf
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo


def test_get_bus_realtime_info_SUCCESS():
    # given
    patcher_get_bus_station_realtime_json = mrf.patcher_get_bus_station_realtime_json()
    patcher_decode_realtime_info_list = mbrs.patcher_decode_realtime_info_list(
        return_value=[],
    )
    patcher_get_bus_station_realtime_json.start()
    patcher_decode_realtime_info_list.start()

    testClient = TestClient(app)
    params = {"station_id": 0}

    # when
    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 200
    # teardown
    patcher_get_bus_station_realtime_json.stop()
    patcher_decode_realtime_info_list.stop()


def test_get_bus_realtime_info_FAIL_STATUS_CODE_500():
    # given
    patcher = mrf.patcher_get_bus_station_realtime_json(side_effect=Exception())
    patcher.start()

    testClient = TestClient(app)
    params = {"station_id": 0}

    # when
    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 500
    # teardown
    patcher.stop()


def test_get_bus_realtime_info_FAIL_STATUS_CODE_501():
    # given
    patcher_get_bus_station_realtime_json = mrf.patcher_get_bus_station_realtime_json()
    patcher_decode_realtime_info_list = mbrs.patcher_decode_realtime_info_list(
        side_effect=Exception(),
    )
    patcher_get_bus_station_realtime_json.start()
    patcher_decode_realtime_info_list.start()

    testClient = TestClient(app)
    params = {"station_id": 0}

    # when
    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 501
    # teardown
    patcher_get_bus_station_realtime_json.stop()
    patcher_decode_realtime_info_list.stop()


def test_get_bus_realtime_info_FAIL_500():
    # given
    patcher_get_seoul_subway_realtime_json = mrf.patcher_get_seoul_subway_realtime_json(
        side_effect=Exception(),
    )
    patcher_get_seoul_subway_realtime_json.start()

    testClient = TestClient(app)
    params = {
        "station_name": "station_name",
        "line_name": "line_name",
        "direction": 1,
    }

    # when
    response = testClient.get(
        "/realtime/get_subway_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 500
    # teardown
    patcher_get_seoul_subway_realtime_json.stop()


def test_get_bus_realtime_info_FAIL_501():
    # given
    patcher_get_seoul_subway_realtime_json = (
        mrf.patcher_get_seoul_subway_realtime_json()
    )
    patcher_filter_subway_realtime_data = msrs.patcher_filter_subway_realtime_data(
        side_effect=Exception(),
    )
    patcher_get_seoul_subway_realtime_json.start()
    patcher_filter_subway_realtime_data.start()

    testClient = TestClient(app)
    params = {
        "station_name": "station_name",
        "line_name": "line_name",
        "direction": 1,
    }

    # when
    response = testClient.get(
        "/realtime/get_subway_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 501
    # teardown
    patcher_get_seoul_subway_realtime_json.stop()
    patcher_filter_subway_realtime_data.stop()


def test_get_bus_realtime_info_SUCCESS():
    # given
    patcher_get_seoul_subway_realtime_json = (
        mrf.patcher_get_seoul_subway_realtime_json()
    )
    patcher_filter_subway_realtime_data = msrs.patcher_filter_subway_realtime_data(
        return_value=RealTimeInfo.mock(),
    )
    patcher_get_seoul_subway_realtime_json.start()
    patcher_filter_subway_realtime_data.start()

    testClient = TestClient(app)
    params = {
        "station_name": "station_name",
        "line_name": "line_name",
        "direction": 1,
    }

    # when
    response = testClient.get(
        "/realtime/get_subway_realtime_info",
        params=params,
    )

    # then
    assert response.status_code == 200
    # teardown
    patcher_get_seoul_subway_realtime_json.stop()
    patcher_filter_subway_realtime_data.stop()
