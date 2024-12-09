from typing import Optional
from sqlalchemy.engine import Engine
from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import Path, Base


class PathCRUD(BaseCRUD):
    def create(
        self,
        user_email: str,
        path: Path,
    ):
        path_table = Path.getTable(
            email=user_email,
            engine=self.engine(),
        )

        stmt = path_table.insert().values(path.to_dict())
        self.session.execute(stmt)
        self.session.flush()

    def update(
        self,
        user_email: str,
        to_update_path: Path,
    ):
        path_table = Path.getTable(
            email=user_email,
            engine=self.engine(),
        )

        stmt = (
            path_table.update()
            .where(path_table.c.id == to_update_path.id)
            .values(to_update_path.to_dict())
        )
        self.session.execute(stmt)
        self.session.flush()

    def read(
        self,
        user_email: str,
        path_id: str,
    ) -> Optional[dict]:
        try:
            path_table = Path.getTable(
                email=user_email,
                engine=self.engine(),
            )
            route_row = (
                self.session.query(path_table).filter(path_table.c.id == path_id).one()
            )
            return route_row._mapping
        except:
            return None

    def delete(
        self,
        user_email: str,
        path_id: str,
    ):
        path_table = Path.getTable(
            email=user_email,
            engine=self.engine(),
        )
        stmt = path_table.delete().where(path_table.c.id == path_id)
        self.session.execute(stmt)
        self.session.flush()

    ### Caution !!! Session Close ###
    @classmethod
    def dropTable(
        cls,
        user_email: str,
        engine: Engine,
    ):
        path_table = Path.getTable(
            email=user_email,
            engine=engine,
        )
        Base.metadata.remove(path_table)
        path_table.drop(bind=engine)

