from eb_fast_api.database.sources.model.models import Schedule, User
from datetime import datetime
from uuid import uuid4


def test_schedule_create_and_read_all(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule_id = str(uuid4())
        schedule = Schedule.mock(id=schedule_id)

        # when
        mockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule,
        )

        # then
        # assert schedule
        fetched_schedule_dict = mockScheduleCRUD.read(
            user_email=user.email,
            schedule_id=schedule_id,
        )
        expect_schedule_dict = schedule.to_dict()
        assert expect_schedule_dict == fetched_schedule_dict

    # delete path, schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockPathCRUD.dropTable(user_email=user.email)


def test_schedule_delete(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule_id = str(uuid4())
        schedule = Schedule.mock(id=schedule_id)
        mockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule,
        )

        # when, then
        fetched_schedule_dict = mockScheduleCRUD.read(
            user_email=user.email,
            schedule_id=schedule_id,
        )
        expect_schedule_dict = schedule.to_dict()
        assert expect_schedule_dict == fetched_schedule_dict

        mockScheduleCRUD.delete(userEmail=user.email, scheduleID=schedule_id)

        try:
            mockScheduleCRUD.read(
                user_email=user.email,
                schedule_id=schedule_id,
            )
            raise Exception("test_schedule_delete_fail")
        except:
            return

    # delete path, schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockPathCRUD.dropTable(user_email=user.email)


def test_schedule_update(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule_id = str(uuid4())
        schedule = Schedule.mock(id=schedule_id)
        mockScheduleCRUD.create(
            userEmail=user.email,
            schedule=schedule,
        )

        # when
        prefix = "to_update"
        schedule.title += prefix
        tmp_time = datetime.fromisoformat("2024-08-28T05:04:32.299Z")
        new_time = tmp_time.replace(microsecond=0, tzinfo=None)
        schedule.time = new_time
        schedule.memo += prefix
        schedule.isNotify = not schedule.isNotify
        schedule.startPlaceID += prefix
        schedule.endPlaceID += prefix
        mockScheduleCRUD.update(userEmail=email, to_update_schedule=schedule)

        # then
        second_fetched_schedule_dict = mockScheduleCRUD.read(
            user_email=user.email,
            schedule_id=schedule_id,
        )
        assert second_fetched_schedule_dict == schedule.to_dict()

    # delete path, schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockPathCRUD.dropTable(user_email=user.email)
