from fastapi import Security, HTTPException
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
