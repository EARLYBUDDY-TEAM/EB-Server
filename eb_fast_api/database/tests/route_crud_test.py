from eb_fast_api.database.sources.model.models import Schedule, Route, User


def test_route_create_and_read(
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
):
    try:
        # given
        user = User.mock(email="email")
        mockUserCRUD.create(user=user)
        mockData = {"test": "test"}
        route = Route.mock(data=mockData)

        # when
        mockRouteCRUD.create(
            user_email=user.email,
            route=route,
        )

        # then
        # assert route
        tmp_fetched_route_list = mockRouteCRUD.read_all(user_email=user.email)
        tmp_fetched_route_dict = tmp_fetched_route_list[0]
        route_id = tmp_fetched_route_dict["id"]
        fetched_route_dict = mockRouteCRUD.read(
            user_email=user.email, route_id=route_id
        )
        assert mockData == fetched_route_dict["data"]

    # delete route table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockRouteCRUD.dropTable(user_email=user.email)
