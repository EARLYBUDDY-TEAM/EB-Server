from sqlalchemy.orm import Session
from eb_fast_api.database.sources.database import EBDataBase


def remove_all_user_data(
    email: str,
    session: Session,
):
    user_crud = EBDataBase.user.createCRUD(session=session)
    user_crud.delete(email=email)

    schedule_crud = EBDataBase.schedule.createCRUD(session=session)
    schedule_crud.dropTable(userEmail=email)

    path_crud = EBDataBase.path.createCRUD(session=session)
    path_crud.dropTable(user_email=email)
