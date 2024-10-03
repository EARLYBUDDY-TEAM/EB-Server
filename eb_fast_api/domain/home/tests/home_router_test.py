from fastapi.testclient import TestClient
from eb_fast_api.main import app
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.domain.token.testings.mock_token_feature import mockGetUserEmail
from eb_fast_api.domain.home.sources.home_schema import ScheduleCard, ScheduleCardList
from eb_fast_api.domain.home.testings.mock_home_feature import (
    scheduleCount,
    mockSchedulCard,
)
from typing import List


def test_get_all_schedule_cards(mock_home_feature):
    app.dependency_overrides[getUserEmail] = mockGetUserEmail

    # when
    testClient = TestClient(app)
    headers = {"access_token": "access_token"}
    response = testClient.get(
        "/home/get_all_schedule_cards",
        headers=headers,
    )

    # then
    expectCards: List[ScheduleCard] = [mockSchedulCard] * scheduleCount
    expectScheduleCardList = ScheduleCardList(scheduleCardList=expectCards)
    expectModel = expectScheduleCardList.model_dump(mode="json")
    responseModel = response.json()
    assert responseModel == expectModel
