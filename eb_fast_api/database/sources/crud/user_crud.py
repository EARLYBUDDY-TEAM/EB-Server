from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import User, Schedule, Base


class UserCRUD(BaseCRUD):
    def create(self, user: User):
        mixinSchedule = Schedule.addToMetaData(email=user.email)
        mixinSchedule.__table__.create(bind=self.engine())
        self.session.add(user)
        self.session.flush()

    def read(self, email: str) -> User:
        user = self.session.query(User).filter(User.email == email).first()
        return user
