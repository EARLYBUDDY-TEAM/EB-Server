from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import (
    RegisterInfo,
    ScheduleInfo,
    PlaceInfo,
)
from datetime import datetime


def test_createSchedule(
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPlaceCRUD,
):
    try:
        # given
        email = "email"
        password = "password"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
        schedule_MockUserCRUD.create(user)
        scheduleInfo = ScheduleInfo.mock()

        # when
        schedule_feature.createSchedule(
            userEmail=email,
            scheduleInfo=scheduleInfo,
            scheduleCRUD=schedule_MockScheduleCRUD,
        )

        # then
        # place
        place_info1 = scheduleInfo.startPlaceInfo
        place_info2 = scheduleInfo.endPlaceInfo
        place_dict1 = schedule_MockPlaceCRUD.read(place_id=place_info1.id)
        place_dict2 = schedule_MockPlaceCRUD.read(place_id=place_info2.id)
        fetched_place_info1 = PlaceInfo.fromPlaceDict(place_dict=place_dict1)
        fetched_place_info2 = PlaceInfo.fromPlaceDict(place_dict=place_dict2)
        assert place_info1 == fetched_place_info1
        assert place_info2 == fetched_place_info2

        fetched_schedule_list = schedule_MockScheduleCRUD.read_all(userEmail=email)
        fetched_schedule_dict = fetched_schedule_list[0]
        expect_schedule = scheduleInfo.toSchedule()
        expect_schedule.id = fetched_schedule_dict["id"]
        assert expect_schedule.to_dict() == fetched_schedule_dict

    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)


def test_update_schedule_with_info(
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPlaceCRUD,
):
    try:
        # given
        email = "email"
        password = "password"
        refreshToken = "refreshToken"
        nickName = "nickName"
        registerInfo = RegisterInfo(
            nickName=nickName,
            email=email,
            password=password,
        )
        user = registerInfo.toUser(refreshToken=refreshToken)
        schedule_MockUserCRUD.create(user)
        scheduleInfo = ScheduleInfo.mock()

        schedule_feature.createSchedule(
            userEmail=email,
            scheduleInfo=scheduleInfo,
            scheduleCRUD=schedule_MockScheduleCRUD,
        )

        # when
        fetched_schedule_list = schedule_MockScheduleCRUD.read_all(userEmail=email)
        fetched_schedule_dict = fetched_schedule_list[0]
        schedule_id = fetched_schedule_dict["id"]

        timeString = "2024-11-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        time = time.replace(microsecond=0, tzinfo=None)
        to_update = ScheduleInfo.mock(id=schedule_id)
        to_update.title = "test_title"
        to_update.memo = "test_memo"
        to_update.isNotify = not to_update.isNotify
        to_update.time = time
        to_update.startPlaceInfo.id = "test_start_id"
        to_update.endPlaceInfo.id = "test_end_id"

        schedule_feature.update_schedule_with_info(
            userEmail=email,
            scheduleInfo=to_update,
            scheduleCRUD=schedule_MockScheduleCRUD,
        )

        # then
        # place
        place_info1 = to_update.startPlaceInfo
        place_info2 = to_update.endPlaceInfo
        place_dict1 = schedule_MockPlaceCRUD.read(place_id=place_info1.id)
        place_dict2 = schedule_MockPlaceCRUD.read(place_id=place_info2.id)
        place1 = place_info1.toPlace()
        place2 = place_info2.toPlace()
        place_dict1["refCount"] = None
        place_dict2["refCount"] = None
        assert place1.to_dict() == place_dict1
        assert place2.to_dict() == place_dict2

        fetched_schedule_list = schedule_MockScheduleCRUD.read_all(userEmail=email)
        fetched_schedule_dict = fetched_schedule_list[0]
        expect_schedule = to_update.toSchedule()
        assert expect_schedule.to_dict() == fetched_schedule_dict

    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
