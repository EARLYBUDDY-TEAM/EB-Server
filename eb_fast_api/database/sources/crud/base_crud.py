from sqlalchemy.orm import Session
from sqlalchemy import Engine


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
