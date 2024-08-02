# import pytest
# from fastapi.testclient import TestClient
# from eb_fast_api.main import app
# from eb_fast_api.database.sources.crud import CRUD
# from eb_fast_api.database.testings.mock_session import mockSession
# from eb_fast_api.domain.auth.login.sources import login_feature


# def getMockDBCRUD():
#     with CRUD(session = mockSession()) as dbCRUD:
#         yield dbCRUD

# @pytest.fixture(scope='session')
# def testClient():
#     app.dependency_overrides[login_feature.getDBCRUD] = getMockDBCRUD
#     yield TestClient(app)