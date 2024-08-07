import pytest
from unittest.mock import patch
from typing import List
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.map.route.sources.route_schema import SubPath, Path, Route
from eb_fast_api.domain.map.route.testings import mock_json


def mockBusSubPath() -> SubPath:
    return SubPath.fromJson(mock_json.subPathBus)


def mockWalkSubPath() -> SubPath:
    return SubPath.fromJson(mock_json.subPathWalk)


def mockSubwaySubPath() -> SubPath:
    return SubPath.fromJson(mock_json.subPathSubway)


def mockSubPathList() -> List[SubPath]:
    return [
        mockWalkSubPath(),
        mockSubwaySubPath(),
        mockWalkSubPath(),
        mockBusSubPath(),
        mockWalkSubPath(),
        mockSubwaySubPath(),
        mockWalkSubPath(),
        mockBusSubPath(),
        mockWalkSubPath(),
    ]


def mockPath() -> Path:
    path = Path.fromJson(mock_json.path)
    path.subPaths = mockSubPathList()
    return path


def mockRoute() -> Route:
    return Route(
        type=0,
        paths=[mockPath()],
    )


@pytest.fixture(scope = 'function')
def fakeGet():
    with patch('eb_fast_api.domain.map.place.sources.place_feature.AsyncClient.get') as get:
        yield get


@pytest.fixture(scope="session")
def testClient():
    testClient = TestClient(app)
    yield testClient
