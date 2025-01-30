from eb_fast_api.main import app
from fastapi.testclient import TestClient
from eb_fast_api.service.realtime.testings import mock_bus_realtime_service as mbrs
from eb_fast_api.service.realtime.testings import mock_subway_realtime_service as msrs
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfoList


def test_get_bus_realtime_info_SUCCESS():
    # given
    mock_realtime_info = RealTimeInfo.mock()
    patcher_request = mbrs.patcher_request(
        return_value=[mock_realtime_info],
    )
    patcher_request.start()

    testClient = TestClient(app)
    params = {"station_id": 0}

    # when
    response = testClient.get(
        "/realtime/get_bus_realtime_info",
        params=params,
    )

    # then
    expect_realtime_info_list = RealTimeInfoList(
        real_time_info_list=[mock_realtime_info],
    )
    assert response.json() == expect_realtime_info_list.model_dump(mode="json")
    assert response.status_code == 200
    # teardown
    patcher_request.stop()


def test_get_bus_realtime_info_FAIL_STATUS_CODE_500():
    # given
    patcher = mbrs.patcher_request(
        side_effect=Exception(),
    )
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


def test_get_subway_realtime_info_SUCCESS():
    # given
    mock_realtime_info = RealTimeInfo.mock()
    patcher_request = msrs.patcher_request(
        return_value=mock_realtime_info,
    )
    patcher_request.start()

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
    expect_realtime_info_list = RealTimeInfoList(
        real_time_info_list=[mock_realtime_info],
    )
    assert response.json() == expect_realtime_info_list.model_dump(mode="json")
    assert response.status_code == 200
    # teardown
    patcher_request.stop()


def test_get_subway_realtime_info_FAIL_STATUS_CODE_500():
    # given
    patcher = msrs.patcher_request(
        side_effect=Exception(),
    )
    patcher.start()

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
    patcher.stop()
