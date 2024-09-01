import pytest, httpx


@pytest.mark.asyncio
def test_searchPlace_SUCCESS(fakeGet, testClient):
    # given
    statusCode = 200
    json = {"test": "test"}
    fakeGet.return_value = httpx.Response(
        statusCode,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    params = {
        "query": "query",
        "x": "x",
        "y": "y",
    }
    response = testClient.get("/map/place/search", params=params)

    # then
    assert response.status_code == statusCode
    assert response.json() == json


@pytest.mark.asyncio
def test_searchPlace_FAIL_client_error(fakeGet, testClient):
    # given
    json = {"test": "test"}
    fakeGet.return_value = httpx.Response(
        410,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    params = {
        "query": "query",
        "x": "x",
        "y": "y",
    }
    response = testClient.get("/map/place/search", params=params)

    # then
    assert response.status_code == 400


@pytest.mark.asyncio
def test_searchPlace_FAIL_server_error(fakeGet, testClient):
    # given
    json = {"test": "test"}
    fakeGet.return_value = httpx.Response(
        510,
        json=json,
        request=httpx.Request("GET", "testURL"),
    )

    # when
    params = {
        "query": "query",
        "x": "x",
        "y": "y",
    }
    response = testClient.get("/map/place/search", params=params)

    # then
    assert response.status_code == 500