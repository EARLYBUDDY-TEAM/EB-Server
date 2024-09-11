from sqlalchemy.orm import Session


class BaseCRUD:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    # db
    def rollback(self):
        self.session.rollback()

    def commit(self):
        print("origin commit")
        self.session.commit()
