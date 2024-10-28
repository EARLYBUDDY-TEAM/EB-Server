import pytest
from unittest.mock import patch
from typing import List
from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schemas import (
    SubPathInfo,
    PathInfo,
    RouteInfo,
)
from eb_fast_api.domain.map.route.testings import mock_json


def mockBusSubPath() -> SubPathInfo:
    return SubPathInfo.fromJson(mock_json.subPathBus)


def mockWalkSubPath() -> SubPathInfo:
    return SubPathInfo.fromJson(mock_json.subPathWalk)


def mockSubwaySubPath() -> SubPathInfo:
    return SubPathInfo.fromJson(mock_json.subPathSubway)


def mockSubPathList() -> List[SubPathInfo]:
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


def mockPath() -> PathInfo:
    path = PathInfo.fromJson(mock_json.path)
    path.subPaths = mockSubPathList()
    return path


def mockRoute() -> RouteInfo:
    return RouteInfo(
        type=0,
        paths=[mockPath()],
    )


@pytest.fixture(scope="function")
def fakeGet():
    with patch(
        "eb_fast_api.domain.map.place.sources.place_feature.AsyncClient.get"
    ) as get:
        yield get


@pytest.fixture(scope="session")
def testClient():
    testClient = TestClient(app)
    yield testClient
