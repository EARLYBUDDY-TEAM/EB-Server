import httpx
from eb_fast_api.domain.map.route.testings import mock_json
from eb_fast_api.domain.schema.sources.schemas import RouteInfo
from eb_fast_api.domain.map.route.sources import route_feature


def test_findRoute_SUCCESS(testClient, fakeGet):
    # given
    statusCode = 200
    json = mock_json.route
    fakeGet.return_value = httpx.Response(
        statusCode,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    startPlace = "startPlace"
    endPlace = "endPlace"
    params = {
        "sx": 1.0,
        "sy": 1.0,
        "ex": 1.0,
        "ey": 1.0,
        "startPlace": startPlace,
        "endPlace": endPlace,
    }
    response = testClient.get("/map/route/find", params=params)

    # then
    mockRoute = RouteInfo.fromJson(json["result"])
    mockRoute = route_feature.refactorRoute(mockRoute, startPlace, endPlace)
    assert response.json() == mockRoute.model_dump(mode="json")
    assert response.status_code == statusCode


def test_findRoute_FAIL_client_error(testClient, fakeGet):
    # given
    json = mock_json.route
    fakeGet.return_value = httpx.Response(
        410,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    startPlace = "startPlace"
    endPlace = "endPlace"
    params = {
        "sx": 1.0,
        "sy": 1.0,
        "ex": 1.0,
        "ey": 1.0,
        "startPlace": startPlace,
        "endPlace": endPlace,
    }
    response = testClient.get("/map/route/find", params=params)

    # then
    assert response.status_code == 400


def test_findRoute_FAIL_server_error(testClient, fakeGet):
    # given
    json = mock_json.route
    fakeGet.return_value = httpx.Response(
        510,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    startPlace = "startPlace"
    endPlace = "endPlace"
    params = {
        "sx": 1.0,
        "sy": 1.0,
        "ex": 1.0,
        "ey": 1.0,
        "startPlace": startPlace,
        "endPlace": endPlace,
    }
    response = testClient.get("/map/route/find", params=params)

    # then
    assert response.status_code == 500
