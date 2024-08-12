from eb_fast_api.snippets.jwt_service.interfaces.abs_jwt_serialization import (
    ABSJWTDecoder,
    ABSJWTEncoder,
)
from eb_fast_api.snippets.jwt_service.sources.jwt_service import JWTService
from datetime import datetime, timedelta


mockTimeString = "2024-07-28T05:04:32.299Z"
mockNow = datetime.fromisoformat(mockTimeString)
mockExpireDate = datetime.timestamp(mockNow)
mockEmail = "test@test.com"


class MockJWTEncoder(ABSJWTEncoder):
    def encode(
        self, data: dict, expireDate: datetime, secretKey: str, algorithm: str
    ) -> str:
        return data["sub"] + str(expireDate)


class MockJWTDecoder(ABSJWTDecoder):
    def decode(self, token: str, secretKey: str, algorithm: str) -> dict | None:
        return {
            "sub": mockEmail,
            "exp": mockExpireDate,
        }


class MockJWTService(JWTService):
    now: datetime

    def __init__(
        self,
        now: datetime = mockNow,
        encoder: ABSJWTEncoder = MockJWTEncoder(),
        decoder: ABSJWTDecoder = MockJWTDecoder(),
    ):
        self.now = now
        super().__init__(
            encoder=encoder,
            decoder=decoder,
        )

    def dateTimeNow(self) -> datetime:
        return self.now
