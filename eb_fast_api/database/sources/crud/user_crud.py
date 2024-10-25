from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import User, Schedule, Path
from typing import Optional


class UserCRUD(BaseCRUD):
    def create(self, user: User):
        mixinSchedule = Schedule.createMixinSchedule(email=user.email)
        mixinSchedule.__table__.create(bind=self.engine())
        mixinRoute = Path.createMixinPath(email=user.email)
        mixinRoute.__table__.create(bind=self.engine())

        self.session.add(user)
        self.session.flush()

    def read(self, email: str) -> Optional[dict]:
        try:
            user = self.session.query(User).filter(User.email == email).one()
            return user.to_dict()
        except:
            return None

    def update(
        self,
        key_email: str,
        nickName: Optional[str] = None,
        hashedPassword: Optional[str] = None,
        refreshToken: Optional[str] = None,
    ):
        user = self.session.query(User).filter(User.email == key_email).first()
        if not user:
            return
        user.nickName = nickName or user.nickName
        user.hashedPassword = hashedPassword or user.hashedPassword
        user.refreshToken = refreshToken or user.refreshToken
        self.session.flush()
        return
