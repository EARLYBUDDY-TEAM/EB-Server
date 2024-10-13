from eb_fast_api.database.sources.model.models import Schedule, Place, User


def test_schedule_create_and_read_all(
    mockSession,
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
        fetched_place_list = mockSession.query(Place).all()
        assert len(fetched_place_list) == 2

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
