import httpx, pytest
from eb_fast_api.domain.map.route.sources import route_feature
from eb_fast_api.domain.map.route.tests import conftest


def test_calTotalWalkTime():
    # given
    mockPath = conftest.mockPath()

    # when
    route_feature.calTotalWalkTime(mockPath)

    # then
    assert mockPath.walkTime == 1 * 5


def test_modifyWalkSubPath_length_one():
    # given
    startPlace = 'startPlace'
    endPlace = 'endPlace'
    subPathWalk = conftest.mockWalkSubPath()

    # when
    route_feature.modifyWalkSubPath([subPathWalk], startPlace, endPlace)

    # then
    assert subPathWalk.startName == startPlace
    assert subPathWalk.endName == endPlace


def test_modifyWalkSubPath_length_more_than_one():
    # given
    startPlace = 'startPlace'
    endPlace = 'endPlace'
    subPaths = conftest.mockSubPathList()

    # when
    route_feature.modifyWalkSubPath(subPaths, startPlace, endPlace)

    # then
    for subPath in subPaths:
        if subPath.type == 3:
            assert subPath.startName != ''
            assert subPath.endName != ''


def test_refactorRoute():
    # given
    mockRoute = conftest.mockRoute()
    startPlace = 'startPlace'
    endPlace = 'endPlace'

    # when
    newRoute = route_feature.refactorRoute(mockRoute, startPlace, endPlace)

    # then
    assert newRoute.paths[0].walkTime == 1 * 5
    for subPath in newRoute.paths[0].subPaths:
        if subPath.type == 3:
            assert subPath.startName != ''
            assert subPath.endName != ''


@pytest.mark.asyncio
async def test_getRouteData(fakeGet):
    # given
    statusCode = 200
    json = {'test' : 'test'}
    fakeGet.return_value = httpx.Response(
        statusCode,
        json = json,
        request = httpx.Request('GET', 'testURL'),
    )

    # when
    response = await route_feature.getRouteData(0, 0, 0, 0)

    # then
    assert response.status_code == statusCode
    assert response.json() == json