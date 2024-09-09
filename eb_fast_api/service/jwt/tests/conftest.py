import pytest
from eb_fast_api.service.jwt.testings.mock_jwt_service import MockJWTService
from eb_fast_api.service.jwt.sources.jwt_service import JWTService


@pytest.fixture(scope="function")
def mockJWTService():
    service = MockJWTService()
    print("Create MockJWTService")
    yield service
    del service
    print("Del MockJWTService")


@pytest.fixture(scope="function")
def realJWTService():
    service = JWTService()
    print("Create RealJWTService")
    yield service
    del service
    print("Del RealJWTService")
