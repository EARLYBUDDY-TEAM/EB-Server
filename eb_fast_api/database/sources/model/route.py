from sqlalchemy import Engine, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Table, MetaData
from typing import Optional, Self
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.connection import engine


class Route:
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)

    def __init__(
        self,
        id: int,
        data: dict,
    ):
        self.id = id
        self.data = data

    @classmethod
    def mock(
        cls,
        id: Optional[int] = None,
        data: Optional[dict] = None,
    ) -> Self:
        mockData = {"mockData": "mockData"}
        return Route(
            id=id or 1,
            data=data or mockData,
        )

    @classmethod
    def getTableName(cls, email: str) -> str:
        return email + "_" + "route"

    @classmethod
    def getTable(
        cls,
        email: str,
        engine: Engine = engine,
    ) -> Table:
        routeTableName = Route.getTableName(email)
        routeMetaData = MetaData()
        routeMetaData.reflect(
            bind=engine,
            only=[routeTableName],
        )
        routeTable = routeMetaData.tables.get(routeTableName)
        if routeTable == None:
            raise Exception(f"No Exist Table : {routeTableName}")
        return routeTable

    @classmethod
    def createMixinRoute(cls, email: str):
        tableName = Route.getTableName(email)

        class MixinRoute(Route, Base):
            __tablename__ = tableName

            @classmethod
            def getTableName(cls) -> str:
                return cls.__table__.name

        return MixinRoute

    def to_dict(self, id: Optional[int] = None) -> dict:
        return {
            "id": id or self.id,
            "data": self.data,
        }
