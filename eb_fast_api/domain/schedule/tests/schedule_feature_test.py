from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import UserInfo, ScheduleInfo
from eb_fast_api.database.sources.model.models import Place, Schedule


def test_createSchedule(scheduleMockDB):
    # given
    email = "email"
    password = "password"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
    scheduleMockDB.userCreate(user)
    scheduleInfo = ScheduleInfo.mock()

    # when
    schedule_feature.createSchedule(
        userEmail=email,
        scheduleInfo=scheduleInfo,
        db=scheduleMockDB,
    )

    # then
    placeCount = scheduleMockDB.session.query(Place).count()
    assert placeCount == 2
    scheduleCount = scheduleMockDB.session.query(Schedule).count()
    assert scheduleCount == 1
    user = scheduleMockDB.userRead(email)
    assert len(user.schedules) == 1
