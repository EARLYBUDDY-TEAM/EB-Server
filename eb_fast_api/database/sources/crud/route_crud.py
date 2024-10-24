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

        stmt = routeTable.insert().values(
            id=route.id,
            data=route.data,
        )
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
