from fastapi.security import APIKeyHeader
from fastapi import Security


mockEmail = "test@test.com"


def mockGetUserEmail(
    token=Security(
        APIKeyHeader(name="access_token"),
    )
) -> str:
    return mockEmail
