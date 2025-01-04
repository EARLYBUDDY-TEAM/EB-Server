import secrets
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jose import jwt, JWTError
from typing import Optional
from eb_fast_api.service.jwt.interfaces.abc_jwt_serialization import (
    ABC_JWTDecoder,
    ABC_JWTEncoder,
)


class JWTEncoder(ABC_JWTEncoder):
    def encode(
        self,
        data: dict,
        expireDate: datetime,
        secretKey: str,
        algorithm: str,
    ) -> str:
        toEncode = data.copy()
        toEncode.update({"exp": expireDate})
        return jwt.encode(toEncode, secretKey, algorithm=algorithm)


class JWTDecoder(ABC_JWTDecoder):
    def decode(
        self,
        token: str,
        secretKey: str,
        algorithm: str,
    ) -> Optional[dict]:
        try:
            return jwt.decode(token, secretKey, algorithms=[algorithm])
        except JWTError:
            return None


class JWTService:
    def __init__(
        self,
        encoder: ABC_JWTEncoder = JWTEncoder(),
        decoder: ABC_JWTDecoder = JWTDecoder(),
        algorithm: str = "HS256",
        secretKey: str = secrets.token_hex(32),
        accessTokenExpireMinute: int = 60,
        refreshTokenExpireDay: int = 14,
    ):
        self.encoder = encoder
        self.decoder = decoder
        self.algorithm = algorithm
        self.secretKey = secretKey
        self.accessTokenExpireMinute = accessTokenExpireMinute
        self.refreshTokenExpireDay = refreshTokenExpireDay

    def dateTimeNow(self) -> datetime:
        return datetime.now(ZoneInfo("Asia/Seoul"))

    def createToken(self, data: dict, expireMinute: int) -> str:
        expireDate = self.dateTimeNow() + timedelta(minutes=expireMinute)
        return self.encoder.encode(
            data,
            expireDate,
            self.secretKey,
            self.algorithm,
        )

    def createAccessToken(self, email: str) -> str:
        data = {"sub": email}
        expireDate = self.dateTimeNow() + timedelta(
            minutes=self.accessTokenExpireMinute
        )
        return self.encoder.encode(
            data,
            expireDate,
            self.secretKey,
            self.algorithm,
        )

    def createRefreshToken(self, email: str) -> str:
        data = {"sub": email}
        expireDate = self.dateTimeNow() + timedelta(days=self.refreshTokenExpireDay)
        return self.encoder.encode(
            data,
            expireDate,
            self.secretKey,
            self.algorithm,
        )

    def checkTokenExpired(self, token: str) -> str:
        # decoded => {'sub': 'test@test.com', 'exp': 1722143072.299}
        decoded = self.decoder.decode(
            token,
            self.secretKey,
            self.algorithm,
        )
        now = datetime.timestamp(self.dateTimeNow())
        return decoded["sub"] if decoded and now < decoded["exp"] else None


jwtService = JWTService()


def getJWTService():
    tmpJWT = JWTService()
    try:
        yield tmpJWT
    finally:
        del tmpJWT
