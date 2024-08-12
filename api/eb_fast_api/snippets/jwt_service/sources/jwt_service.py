from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jose import jwt, JWTError
import secrets
from typing import Optional
from eb_fast_api.snippets.jwt_service.interfaces.abs_jwt_serialization import (
    ABSJWTDecoder,
    ABSJWTEncoder,
)


class JWTEncoder(ABSJWTEncoder):
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


class JWTDecoder(ABSJWTDecoder):
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
        encoder: ABSJWTEncoder = JWTEncoder(),
        decoder: ABSJWTDecoder = JWTDecoder(),
        algorithm: str = "HS256",
        secretKey: str = secrets.token_hex(32),
        accessTokenExpireMinute: int = 20,
        refreshTokenExpireMinute: int = 10,
    ):
        self.encoder = encoder
        self.decoder = decoder
        self.algorithm = algorithm
        self.secretKey = secretKey
        self.accessTokenExpireMinute = accessTokenExpireMinute
        self.refreshTokenExpireMinute = refreshTokenExpireMinute

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
        return self.createToken(
            data,
            self.accessTokenExpireMinute,
        )

    def createRefreshToken(self, email: str) -> str:
        data = {"sub": email}
        return self.createToken(
            data,
            self.refreshTokenExpireMinute,
        )

    def checkTokenExpired(self, token: str) -> Optional[dict]:
        decoded = self.decoder.decode(
            token,
            self.secretKey,
            self.algorithm,
        )
        now = datetime.timestamp(self.dateTimeNow())
        return decoded if decoded and now < decoded["exp"] else None
