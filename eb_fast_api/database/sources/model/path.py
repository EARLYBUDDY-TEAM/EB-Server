from sqlalchemy import Engine, JSON, Column, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Table, MetaData
from typing import Optional, Self
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.connection import engine
from uuid import uuid4


class Path:
    id = Column(String(50), primary_key=True)
    data: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)

    def __init__(
        self,
        id: str,
        data: dict,
    ):
        self.id = id
        self.data = data

    @classmethod
    def mock(
        cls,
        id: Optional[str] = None,
        data: Optional[dict] = None,
    ) -> Self:
        mockData = {"mockData": "mockData"}
        return Path(
            id=id or str(uuid4()),
            data=data or mockData,
        )

    @classmethod
    def getTableName(cls, email: str) -> str:
        return email + "_" + "path"

    @classmethod
    def getTable(
        cls,
        email: str,
        engine: Engine = engine,
    ) -> Table:
        pathTableName = Path.getTableName(email)
        pathMetaData = MetaData()
        pathMetaData.reflect(
            bind=engine,
            only=[pathTableName],
        )
        pathTable = pathMetaData.tables.get(pathTableName)
        if pathTable == None:
            raise Exception(f"No Exist Table : {pathTableName}")
        return pathTable

    @classmethod
    def createMixinPath(cls, email: str):
        tableName = Path.getTableName(email)

        class MixinPath(Path, Base):
            __tablename__ = tableName

            @classmethod
            def getTableName(cls) -> str:
                return cls.__table__.name

        return MixinPath

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "data": self.data,
        }
