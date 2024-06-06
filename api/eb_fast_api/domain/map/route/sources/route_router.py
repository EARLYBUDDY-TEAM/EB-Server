from fastapi import APIRouter
from eb_fast_api.domain.map.route.sources import route_feature

router = APIRouter(prefix='/map/route')

@router.get('/search')
async def search_route():
    return 'success'