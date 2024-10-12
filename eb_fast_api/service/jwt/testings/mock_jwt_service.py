from eb_fast_api.service.jwt.interfaces.abc_jwt_serialization import (
    ABC_JWTDecoder,
    ABC_JWTEncoder,
)
from eb_fast_api.service.jwt.sources.jwt_service import JWTService
from datetime import datetime, timedelta


mockTimeString = "2024-07-28T05:04:32.299Z"
mockNow = datetime.fromisoformat(mockTimeString)
mockExpireDate = datetime.timestamp(mockNow)
mockEmail = "test@test.com"


class MockJWTEncoder(ABC_JWTEncoder):
    def encode(
        self, data: dict, expireDate: datetime, secretKey: str, algorithm: str
    ) -> str:
        return data["sub"] + str(expireDate)


class MockJWTDecoder(ABC_JWTDecoder):
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
        encoder: ABC_JWTEncoder = MockJWTEncoder(),
        decoder: ABC_JWTDecoder = MockJWTDecoder(),
    ):
        super().__init__(
            encoder=encoder,
            decoder=decoder,
        )
        self.now = now

    def dateTimeNow(self) -> datetime:
        return self.now
