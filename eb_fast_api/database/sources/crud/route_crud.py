from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import Route, Base
from typing import List


class RouteCRUD(BaseCRUD):
    def create(
        self,
        user_email: str,
        route: Route,
    ):
        routeTable = Route.getTable(
            email=user_email,
            engine=self.engine(),
        )

        stmt = routeTable.insert().values(data=route.data)
        self.session.execute(stmt)
        self.session.flush()

    def read(
        self,
        user_email: str,
        route_id: int,
    ) -> dict:
        route_table = Route.getTable(
            email=user_email,
            engine=self.engine(),
        )
        route_row = (
            self.session.query(route_table).filter(route_table.c.id == route_id).one()
        )
        return route_row._mapping

    def read_all(self, user_email: str) -> List[dict]:
        route_table = Route.getTable(
            email=user_email,
            engine=self.engine(),
        )
        route_row_list = self.session.query(route_table).all()
        return [row._mapping for row in route_row_list]

    ### Caution !!! Session Close ###
    def dropTable(
        self,
        user_email: str,
    ):
        self.session.close()
        routeTable = Route.getTable(
            email=user_email,
            engine=self.engine(),
        )
        Base.metadata.remove(routeTable)
        routeTable.drop(bind=self.engine())
