from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.database.sources.model import User, Schedule
from eb_fast_api.snippets.sources import pwdcrypt


# def test_createSchedule_SUCCESS(scheduleMockDB):
#     # given
#     email = 'email'
#     password = 'password'
#     user = User(userEmail=email, hashedPassword=pwdcrypt.hash(password),)
#     scheduleMockDB.userCreate(user)
#     schedule = Schedule.mock()

#     schedule_feature.createSchedule(userEmail=email, s)
#     return
