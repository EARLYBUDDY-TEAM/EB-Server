from eb_fast_api.domain.auth.sources.auth_feature.remove_user_feature import (
    remove_all_user_data,
)
from eb_fast_api.database.sources.model.models import User, Schedule, Path
from sqlalchemy import inspect
from sqlalchemy.orm import Session


# def check_table_exists(
#     table_name: str,
#     session: Session,
# ):
#     engine = session.get_bind()
#     return inspect(engine).has_table(table_name)


# def test_remove_all_user_data(
#     authMockUserCRUD,
#     authMockScheduleCRUD,
#     authMockPathCRUD,
#     authMockSession,
# ):
#     try:
#         # given
#         mock_user = User.mock()
#         authMockUserCRUD.create(user=mock_user)

#         # when
#         remove_all_user_data(
#             email=mock_user.email,
#             session=authMockSession,
#         )

#         # then
#         schedule_table_name = Schedule.getTableName(email=mock_user.email)
#         is_schedule_table_exists = check_table_exists(
#             table_name=schedule_table_name,
#             session=authMockSession,
#         )
#         path_table_name = Path.getTableName(email=mock_user.email)
#         is_path_table_exists = check_table_exists(
#             table_name=path_table_name,
#             session=authMockSession,
#         )
#         assert is_schedule_table_exists == False
#         assert is_path_table_exists == False
#     finally:
#         try:
#             authMockScheduleCRUD.dropTable(userEmail=mock_user.email)
#             authMockPathCRUD.dropTable(user_email=mock_user.email)
#         except Exception as e:
#             print(f"test_remove_all_user_data, finally exception: {e}")
