from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import UserInfo, ScheduleInfo
from eb_fast_api.database.sources.model.models import Place, Schedule


def test_createSchedule(schedule_MockUserCRUD, schedule_MockScheduleCRUD,):
    # given
    email = "email"
    password = "password"
    userInfo = UserInfo(email, password)
    user = userInfo.toUser()
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
    scheduleCount = schedule_MockScheduleCRUD.session.query(Schedule).count()
    assert scheduleCount == 1
    user = schedule_MockUserCRUD.read(email)
    assert len(user.schedules) == 1
