import pytest
from eb_fast_api.service.jwt.sources.jwt_service import JWTService


@pytest.fixture(scope="function")
def realJWTService():
    service = JWTService()
    print("Create RealJWTService")
    yield service
    del service
    print("Del RealJWTService")
