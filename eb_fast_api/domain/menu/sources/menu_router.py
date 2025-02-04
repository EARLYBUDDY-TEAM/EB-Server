from fastapi import APIRouter
from eb_fast_api.domain.menu.sources.sub_routers.noti_status.sources import (
    noti_status_router,
)


router = APIRouter()


def with_prefix(my_prefix: str) -> str:
    return f"/menu/{my_prefix}"


router.include_router(noti_status_router.router, prefix=with_prefix("noti_status"))
