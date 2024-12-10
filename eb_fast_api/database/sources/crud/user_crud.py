from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import User, Schedule, Path
from typing import Optional, List


class UserCRUD(BaseCRUD):
    def create(
        self,
        user: User,
    ):
        mixinSchedule = Schedule.createMixinSchedule(email=user.email)
        mixinSchedule.__table__.create(bind=self.engine)
        mixinPath = Path.createMixinPath(email=user.email)
        mixinPath.__table__.create(bind=self.engine)

        self.__delete_exist_fcm_token(fcm_token=user.fcm_token)
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
        fcm_token: Optional[str] = None,
    ):
        self.__delete_exist_fcm_token(fcm_token=fcm_token)

        user = self.session.query(User).filter(User.email == key_email).first()
        if not user:
            raise Exception("User not found")

        user.nickName = nickName or user.nickName
        user.hashedPassword = hashedPassword or user.hashedPassword
        user.refreshToken = refreshToken or user.refreshToken
        user.fcm_token = fcm_token or user.fcm_token
        self.session.flush()

    def read_all(self) -> List[dict]:
        user_list = self.session.query(User).all()
        return [user.to_dict() for user in user_list]

    def __delete_exist_fcm_token(
        self,
        fcm_token: Optional[str],
    ):
        if not fcm_token:
            return

        user_own_fcm_token = (
            self.session.query(User).filter(User.fcm_token == fcm_token).first()
        )
        if not user_own_fcm_token:
            return

        user_own_fcm_token.fcm_token = None
        self.session.flush()

    ### Caution !!! Session Close ###
    def delete(
        self,
        email: str,
    ):
        self.session.query(User).filter(User.email == email).delete()
        self.session.commit()
        self.session.close()

        Schedule.dropTable(
            user_email=email,
            engine=self.engine,
        )
        Path.dropTable(
            user_email=email,
            engine=self.engine,
        )
