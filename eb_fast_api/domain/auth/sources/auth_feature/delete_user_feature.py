from eb_fast_api.database.sources.crud.cruds import UserCRUD
from typing import Callable


def delete_user_data_in_db(
    user_email: str,
    user_crud: UserCRUD,
    def_create_engine: Callable,
):
    user_crud.delete(
        email=user_email,
        def_create_engine=def_create_engine,
    )
