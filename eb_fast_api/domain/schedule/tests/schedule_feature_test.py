from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import UserInfo, ScheduleInfo
from eb_fast_api.database.sources.model.models import Place, Schedule


def test_createSchedule(scheduleMockScheduleCRUD, scheduleMockUserCRUD):
    # given
    email = "email"
    password = "password"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
    scheduleMockUserCRUD.create(user)
    scheduleInfo = ScheduleInfo.mock()

    # when
    schedule_feature.createSchedule(
        userEmail=email,
        scheduleInfo=scheduleInfo,
        scheduleCRUD=scheduleMockScheduleCRUD,
    )

    # then
    placeCount = scheduleMockScheduleCRUD.session.query(Place).count()
    assert placeCount == 2
    scheduleCount = scheduleMockScheduleCRUD.session.query(Schedule).count()
    assert scheduleCount == 1
    user = scheduleMockUserCRUD.read(email)
    assert len(user.schedules) == 1
