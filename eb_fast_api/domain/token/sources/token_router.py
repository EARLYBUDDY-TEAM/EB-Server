from fastapi import APIRouter, Depends
from eb_fast_api.domain.token.sources.token_feature import verifyToken


router = APIRouter(prefix="/test_token_service")


@router.get("/test_token")
def test_token(userEmail=Depends(verifyToken)):
    return {"userEmail": userEmail}
