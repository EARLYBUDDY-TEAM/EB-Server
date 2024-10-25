from eb_fast_api.database.sources.model.models import Path, User
from uuid import uuid4


def test_path_create_and_read(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
):
    try:
        # given
        user = User.mock(email="email")
        mockUserCRUD.create(user=user)
        mock_data = {"test": "test"}
        path_id = str(uuid4())
        path = Path.mock(
            id=path_id,
            data=mock_data,
        )

        # when
        mockPathCRUD.create(
            user_email=user.email,
            path=path,
        )

        # then
        # assert path
        fetched_path_dict = mockPathCRUD.read(
            user_email=user.email,
            path_id=path_id,
        )
        assert mock_data == fetched_path_dict["data"]

    # delete path, schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockPathCRUD.dropTable(user_email=user.email)


def test_path_update(
    mockUserCRUD,
    mockScheduleCRUD,
    mockPathCRUD,
):
    try:
        # given
        user = User.mock(email="email")
        mockUserCRUD.create(user=user)
        mock_data = {"test": "test"}
        path_id = str(uuid4())
        path = Path.mock(
            id=path_id,
            data=mock_data,
        )
        mockPathCRUD.create(
            user_email=user.email,
            path=path,
        )

        # when
        to_update_data = {"to_update_data": "to_update_data"}
        path.data = to_update_data
        mockPathCRUD.update(
            user_email=user.email,
            to_update_path=path,
        )

        # then
        # assert path
        fetched_path_dict = mockPathCRUD.read(
            user_email=user.email,
            path_id=path_id,
        )
        assert to_update_data == fetched_path_dict["data"]

    # delete path, schedule table
    finally:
        mockScheduleCRUD.dropTable(userEmail=user.email)
        mockPathCRUD.dropTable(user_email=user.email)
