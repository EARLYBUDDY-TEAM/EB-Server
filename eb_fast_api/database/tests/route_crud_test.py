from eb_fast_api.database.sources.model.models import Route, User


def test_route_create_and_read(
    mockUserCRUD,
    mockScheduleCRUD,
    mockRouteCRUD,
):
    try:
        # given
        user = User.mock(email="email")
        mockUserCRUD.create(user=user)
        mock_data = {"test": "test"}
        route_id = 10
        route = Route.mock(
            id=route_id,
            data=mock_data,
        )

        # when
        mockRouteCRUD.create(
            user_email=user.email,
            route=route,
        )

        # then
        # assert route
        fetched_route_dict = mockRouteCRUD.read(
            user_email=user.email, route_id=route_id
        )
        assert mock_data == fetched_route_dict["data"]

    # delete route table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockRouteCRUD.dropTable(user_email=user.email)
