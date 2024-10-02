# from fastapi.testclient import TestClient
# from eb_fast_api.main import app
# from eb_fast_api.domain.schema.sources.schema import ScheduleInfo, RegisterInfo
# from eb_fast_api.database.sources.database import EBDataBase
# from eb_fast_api.database.sources.model.models import Schedule
# from eb_fast_api.domain.token.sources.token_feature import getUserEmail
# from eb_fast_api.domain.token.testings.mock_token_feature import (
#     mockGetUserEmail,
#     mockEmail,
# )
# from eb_fast_api.domain.home.sources import home_feature
# from eb_fast_api.domain.home.sources.home_schema import ScheduleCard


# def test_get_all_schedule_cards(
#     # home_MockUserCRUD,
#     home_MockScheduleCRUD,
#     home_MockPlaceCRUD,
# ):
#     # def test_get_all_schedule_cards():
#     # given, create mockdata
#     scheduleCount = 5
#     mockScheduleList = [Schedule.mock() for _ in range(scheduleCount)]
#     mockSchedulCardList = [ScheduleCard.mock() for _ in mockScheduleList]

#     # given, inject dependencies
#     def mock_read_all_schedule(
#         userEmail,
#         scheduleCRUD,
#     ):
#         return mockScheduleList

#     def mock_schedule_to_schedulecard(
#         schedule,
#         placeCRUD,
#     ):
#         return mockSchedulCardList

#     def getMockScheduleCRUD():
#         yield home_MockScheduleCRUD

#     def getMockPlaceCRUD():
#         yield home_MockPlaceCRUD

#     app.dependency_overrides[EBDataBase.schedule.getCRUD] = getMockScheduleCRUD
#     app.dependency_overrides[EBDataBase.place.getCRUD] = getMockPlaceCRUD

#     app.dependency_overrides[getUserEmail] = mockGetUserEmail
#     app.dependency_overrides[home_feature.read_all_schedule] = mock_read_all_schedule
#     app.dependency_overrides[home_feature.schedule_to_schedulecard] = (
#         mock_schedule_to_schedulecard
#     )
#     testClient = TestClient(app)

#     # when
#     headers = {"access_token": "access_token"}
#     response = testClient.get(
#         "/home/get_all_schedule_cards",
#         headers=headers,
#     )

#     # then
#     responseModel = response.json()
#     print(responseModel)

#     # # given, add mock data
#     # email = mockEmail
#     # password = "password"
#     # refreshToken = "refreshToken"
#     # name = "name"
#     # registerInfo = RegisterInfo(
#     #     name=name,
#     #     email=email,
#     #     password=password,
#     # )
#     # user = registerInfo.toUser(refreshToken=refreshToken)
#     # home_MockUserCRUD.create(user)

#     # scheduleCount = 5
#     # for _ in range(scheduleCount):
#     #     home_MockScheduleCRUD.create(
#     #         userEmail=email,
#     #         schedule=Schedule.mock(),
#     #         startPlace=None,
#     #         endPlace=None,
#     #     )

#     # # given, inject dependencies
#     # def getMockScheduleDB():
#     #     yield home_MockScheduleCRUD

#     # app.dependency_overrides[EBDataBase.schedule.getCRUD] = getMockScheduleDB
#     # app.dependency_overrides[getUserEmail] = mockGetUserEmail

#     # testClient = TestClient(app)

#     # # when
#     # headers = {"access_token": "access_token"}
#     # response = testClient.get(
#     #     "/home/get_all_schedule_cards",
#     #     headers=headers,
#     # )

#     # # then
#     # responseModel = response.json()
#     # print(responseModel)
#     # responseScheduleCardList = responseModel["scheduleCardList"]
#     # assert len(responseScheduleCardList) == scheduleCount

#     # # restore dependencies
#     # del app.dependency_overrides[EBDataBase.schedule.getCRUD]
#     # del app.dependency_overrides[getUserEmail]

#     # # delete schedule table
#     # home_MockScheduleCRUD.dropTable(userEmail=email)
