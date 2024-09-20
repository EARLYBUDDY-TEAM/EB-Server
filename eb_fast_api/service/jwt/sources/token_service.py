from fastapi import Security, HTTPException, APIRouter, Depends
from fastapi.security import APIKeyHeader
from eb_fast_api.service.jwt.sources.jwt_service import jwtService


def verifyToken(
    token=Security(
        APIKeyHeader(name="access-token"),
    )
) -> str:
    email = jwtService.checkTokenExpired(token)
    if email == None:
        raise HTTPException(
            status_code=490,
            detail="토큰 만료",
        )
    else:
        return email


router = APIRouter(prefix="/test_token_service")


@router.get("/test_token")
def test_token(userEmail=Depends(verifyToken)):
    return {"userEmail": userEmail}
