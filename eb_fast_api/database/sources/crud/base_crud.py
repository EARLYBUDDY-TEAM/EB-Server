from sqlalchemy.orm import Session
from sqlalchemy import Engine, inspect


class BaseCRUD:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def engine(self) -> Engine:
        return self.session.get_bind()

    def rollback(self):
        self.session.rollback()

    def commit(self):
        self.session.commit()

    # def object_as_dict(obj):
    #     return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
