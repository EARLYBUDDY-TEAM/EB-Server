from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import User


class UserCRUD(BaseCRUD):
    def create(self, user: User):
        self.session.add(user)
        self.session.flush()

    def read(self, email: str) -> User:
        user = self.session.query(User).filter(User.email == email).first()
        return user
