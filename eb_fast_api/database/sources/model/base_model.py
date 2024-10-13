from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    __abstract__ = True

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
