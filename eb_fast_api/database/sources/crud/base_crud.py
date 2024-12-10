from sqlalchemy.orm import Session
from sqlalchemy import Engine


class BaseCRUD:
    session: Session
    engine: Engine

    def __init__(
        self,
        session: Session,
        engine: Engine,
    ):
        self.session = session
        self.engine = engine

    def rollback(self):
        self.session.rollback()

    def commit(self):
        self.session.commit()
