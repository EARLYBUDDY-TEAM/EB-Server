from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import (
    RegisterInfo,
    ScheduleInfo,
    PlaceInfo,
)
from eb_fast_api.database.sources.model.models import Place, Schedule


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

        place_info1 = scheduleInfo.startPlaceInfo
        place_info2 = scheduleInfo.endPlaceInfo
        place_dict1 = schedule_MockPlaceCRUD.read(place_id=place_info1.id)
        place_dict2 = schedule_MockPlaceCRUD.read(place_id=place_info2.id)
        fetched_place_info1 = PlaceInfo.fromPlaceDict(place_dict=place_dict1)
        fetched_place_info2 = PlaceInfo.fromPlaceDict(place_dict=place_dict2)
        assert place_info1 == fetched_place_info1
        assert place_info2 == fetched_place_info2

        mockEngine = schedule_MockScheduleCRUD.engine()
        scheduleTable = Schedule.getTable(
            email=email,
            engine=mockEngine,
        )
        scheduleCount = schedule_MockScheduleCRUD.session.query(scheduleTable).count()
        assert scheduleCount == 1

    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
