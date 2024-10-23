from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.schema.sources.schemas import RegisterInfo
from eb_fast_api.database.sources.database import EBDataBase


def test_register_FAIL_invalid_register_info(testClient):
    invalidEmail = "abc@abc"
    password = "password12"
    nickName = "nickName"
    registerInfo = RegisterInfo(
        nickName=nickName,
        email=invalidEmail,
        password=password,
    )
    json = registerInfo.model_dump(mode="json")
    response = testClient.post("/auth/register", json=json)

    assert response.status_code == 400


def test_register_FAIL_exist_user(
    registerMockUserCRUD,
    registerMockScheduleCRUD,
    registerMockRouteCRUD,
):
    try:
        # given
        email = "test@test.com"
        password = "password12"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
        registerMockUserCRUD.create(user)

        def getMockRegisterCRUD():
            yield registerMockUserCRUD

        app.dependency_overrides[EBDataBase.user.getCRUD] = getMockRegisterCRUD
        testClient = TestClient(app)

        # when
        json = registerInfo.model_dump(mode="json")
        response = testClient.post("/auth/register", json=json)

        # then
        assert response.status_code == 401
        del app.dependency_overrides[EBDataBase.user.getCRUD]

    finally:
        # delete schedule, route table
        registerMockScheduleCRUD.dropTable(userEmail=email)
        registerMockRouteCRUD.dropTable(user_email=email)


def test_register_SUCCESS(
    testClient,
    registerMockScheduleCRUD,
    registerMockRouteCRUD,
):
    try:
        # given
        email = "test@test.com"
        password = "password12"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        json = registerInfo.model_dump(mode="json")

        # when
        response = testClient.post("/auth/register", json=json)

        # then
        assert response.status_code == 200

    finally:
        # delete schedule, route table
        registerMockScheduleCRUD.dropTable(userEmail=email)
        registerMockRouteCRUD.dropTable(user_email=email)
