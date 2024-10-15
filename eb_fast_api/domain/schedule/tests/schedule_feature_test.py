from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import RegisterInfo, ScheduleInfo
from eb_fast_api.database.sources.model.models import Place, Schedule


def test_createSchedule(
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
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
        placeCount = schedule_MockScheduleCRUD.session.query(Place).count()
        assert placeCount == 2
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
