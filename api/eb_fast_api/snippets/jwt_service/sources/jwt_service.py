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
        expireDelta: int,
        secretKey: str,
        algorithm: str,
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(ZoneInfo("Asia/Seoul")) + timedelta(minutes=expireDelta)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, secretKey, algorithm=algorithm)


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

    def __del__(self):
        print("DEL JWTService Instance")

    def __createToken(self, data: dict, expireDelta: int) -> str:
        return self.encoder.encode(
            data,
            expireDelta,
            self.secretKey,
            self.algorithm,
        )

    def createAccessToken(self, email: str) -> str:
        data = {"sub": email}
        return self.__createToken(
            data,
            self.accessTokenExpireMinute,
        )

    def createRefreshToken(self, email: dict) -> str:
        data = {"sub": email}
        return self.__createToken(
            data,
            self.refreshTokenExpireMinute,
        )

    def checkTokenExpired(self, token: str) -> Optional[dict]:
        payload = self.decoder.decode(
            token,
            self.secretKey,
            self.algorithm,
        )
        now = datetime.timestamp(datetime.now(ZoneInfo("Asia/Seoul")))
        return None if payload and payload["exp"] < now else payload
