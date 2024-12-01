from eb_fast_api.domain.schedule.sources.schedule_feature.delete.delete_schedule import (
    delete_schedule,
)
from eb_fast_api.domain.schema.sources.schemas import (
    RegisterInfo,
    PathInfo,
)
from eb_fast_api.database.sources.model.models import Schedule
from uuid import uuid4


def test_delete_schedule(
    schedule_MockSession,
    schedule_MockUserCRUD,
    schedule_MockScheduleCRUD,
    schedule_MockPathCRUD,
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
        schedule_MockUserCRUD.create(user=user)

        path_info = PathInfo.mock()
        schedule_id = str(uuid4())
        schedule = Schedule.mock(id=schedule_id)
        schedule_MockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule,
        )
        path = path_info.to_path(id=schedule_id)
        schedule_MockPathCRUD.create(
            user_email=user.email,
            path=path,
        )

        # when
        delete_schedule(
            session=schedule_MockSession,
            user_email=user.email,
            schedule_id=schedule_id,
        )

        # then
        try:
            schedule_MockScheduleCRUD.read(
                user_email=user.email, schedule_id=schedule_id
            )
            raise Exception("test_delete_schedule_fail")
        except:
            pass

        fetched_path_dict = schedule_MockPathCRUD.read(
            user_email=user.email,
            path_id=schedule_id,
        )
        if fetched_path_dict:
            raise Exception("test_delete_schedule_fail")
        else:
            return
    # delete schedule table
    finally:
        schedule_MockScheduleCRUD.dropTable(userEmail=email)
        schedule_MockPathCRUD.dropTable(user_email=email)
