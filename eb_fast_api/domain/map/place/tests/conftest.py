import pytest
from unittest.mock import patch
from eb_fast_api.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope = 'function')
def fakeGet():
    with patch('eb_fast_api.domain.map.place.sources.place_feature.AsyncClient.get') as get:
        yield get


@pytest.fixture(scope = 'session')
def testClient():
    testClient = TestClient(app)
    yield testClient