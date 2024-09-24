from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import User, Schedule
from typing import Optional


class UserCRUD(BaseCRUD):
    def create(self, user: User):
        mixinSchedule = Schedule.createMixinSchedule(email=user.email)
        mixinSchedule.__table__.create(bind=self.engine())
        self.session.add(user)
        self.session.flush()

    def read(self, email: str) -> Optional[User]:
        user = self.session.query(User).filter(User.email == email).first()
        return user

    def update(
        self,
        key_email: str,
        hashedPassword: Optional[str] = None,
        refreshToken: Optional[str] = None,
    ):
        user = self.read(email=key_email)
        user.hashedPassword = hashedPassword or user.hashedPassword
        user.refreshToken = refreshToken or user.refreshToken
        self.session.flush()
        return
