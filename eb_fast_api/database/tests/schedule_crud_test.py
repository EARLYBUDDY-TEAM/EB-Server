from eb_fast_api.database.sources.model.models import Schedule, Place, User
from datetime import datetime


def test_schedule_create_and_read_all(
    mockPlaceCRUD,
    mockUserCRUD,
    mockScheduleCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule = Schedule.mock()
        startPlace = Place.mock(id="mockStartPlace")
        endPlace = Place.mock(id="mockEndPlace")
        schedule.startPlaceID = startPlace.id
        schedule.endPlaceID = endPlace.id

        # when
        mockScheduleCRUD.create(
            userEmail=email,
            schedule=schedule,
            startPlace=startPlace,
            endPlace=endPlace,
        )

        # then
        # assert place
        fetched_start_place_dict = mockPlaceCRUD.read(place_id=startPlace.id)
        assert startPlace.to_dict() == fetched_start_place_dict
        fetched_end_place_dict = mockPlaceCRUD.read(place_id=endPlace.id)
        assert endPlace.to_dict() == fetched_end_place_dict

        # # assert schedule
        fetched_schedule_dict_list = mockScheduleCRUD.read_all(userEmail=email)
        fetched_schedule_dict = fetched_schedule_dict_list[0]
        schedule_id = fetched_schedule_dict["id"]
        expect_schedule_dict = schedule.to_dict(id=schedule_id)

        print(expect_schedule_dict)
        print(fetched_schedule_dict)
        # assert expect_schedule_dict == fetched_schedule_dict

    # delete schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)


def test_schedule_delete(
    mockUserCRUD,
    mockScheduleCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule = Schedule.mock()
        startPlace = Place.mock(id="mockStartPlace")
        endPlace = Place.mock(id="mockEndPlace")
        schedule.startPlaceID = startPlace.id
        schedule.endPlaceID = endPlace.id
        mockScheduleCRUD.create(
            userEmail=email,
            schedule=schedule,
            startPlace=startPlace,
            endPlace=endPlace,
        )

        # when, then
        fetched_schedule_dict_list = mockScheduleCRUD.read_all(userEmail=email)
        assert len(fetched_schedule_dict_list) == 1

        fetched_schedule_dict = fetched_schedule_dict_list[0]
        schedule_id = fetched_schedule_dict["id"]
        mockScheduleCRUD.delete(userEmail=email, scheduleID=schedule_id)

        fetched_schedule_dict_list = mockScheduleCRUD.read_all(userEmail=email)
        assert len(fetched_schedule_dict_list) == 0

    # delete schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)


def test_schedule_update(
    mockUserCRUD,
    mockScheduleCRUD,
):
    try:
        # given
        email = "email"
        user = User.mock(email=email)
        mockUserCRUD.create(user=user)
        schedule = Schedule.mock()
        startPlace = Place.mock(id="mockStartPlace")
        endPlace = Place.mock(id="mockEndPlace")
        schedule.startPlaceID = startPlace.id
        schedule.endPlaceID = endPlace.id
        mockScheduleCRUD.create(
            userEmail=email,
            schedule=schedule,
            startPlace=startPlace,
            endPlace=endPlace,
        )
        fetched_schedule_list = mockScheduleCRUD.read_all(userEmail=email)
        fetched_schedule_dict = fetched_schedule_list[0]
        schedule_id = fetched_schedule_dict["id"]
        schedule.id = schedule_id

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
        mockScheduleCRUD.update(userEmail=email, schedule=schedule)

        # then
        second_fetched_schedule_list = mockScheduleCRUD.read_all(userEmail=email)
        second_fetched_schedule_dict = second_fetched_schedule_list[0]
        assert second_fetched_schedule_dict == schedule.to_dict()

    # delete schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
