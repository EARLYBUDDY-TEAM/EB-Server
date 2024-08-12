import pytest
from eb_fast_api.snippets.jwt_service.testings.mock_jwt_service import MockJWTService


@pytest.fixture(scope='function')
def mockJWTService():
    service = MockJWTService()
    print('Create MockJWTService')
    yield service
    del service
    print('Del MockJWTService')