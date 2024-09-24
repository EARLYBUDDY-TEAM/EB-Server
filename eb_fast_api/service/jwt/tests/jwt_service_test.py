import secrets
from eb_fast_api.service.jwt.sources.jwt_service import JWTDecoder, JWTEncoder
from eb_fast_api.service.jwt.testings.mock_jwt_service import (
    MockJWTService,
    mockNow,
    mockEmail,
)
from typing import Optional
from datetime import datetime, timedelta


class TestJWTSerialization:
    encoder = JWTEncoder()
    decoder = JWTDecoder()
    algorithm: str = "HS256"
    secretKey: str = secrets.token_hex(32)

    def test_serialize_SUCCESS(self):
        # given
        testEmail = "test@test.com"
        data = {"sub": testEmail}
        expireDate = datetime.now()
        exp = int(datetime.timestamp(expireDate))

        # when, then
        try:
            token = self.encoder.encode(
                data=data,
                expireDate=expireDate,
                secretKey=self.secretKey,
                algorithm=self.algorithm,
            )

            decoded: Optional[dict] = self.decoder.decode(
                token=token,
                secretKey=self.secretKey,
                algorithm=self.algorithm,
            )
            if decoded == None:
                raise Exception("fail test ...")
            assert decoded["sub"] == testEmail
            assert decoded["exp"] == exp
        except:
            raise Exception("fail test ...")


class TestJWTService:
    jwtService = MockJWTService()

    def test_calDateTimeNow(self, mockJWTService):
        result = mockJWTService.dateTimeNow()
        assert result == mockNow

    def test_createToken(self, mockJWTService):
        expireMinute = 10
        expireDate = mockJWTService.dateTimeNow() + timedelta(minutes=expireMinute)
        data = {
            "sub": mockEmail,
            "exp": expireDate,
        }

        result = mockJWTService.createToken(data=data, expireMinute=expireMinute)

        assert result == data["sub"] + str(expireDate)

    def test_createAccessToken(self, mockJWTService):
        result = mockJWTService.createAccessToken(email=mockEmail)
        expireDate = mockJWTService.dateTimeNow() + timedelta(
            minutes=mockJWTService.accessTokenExpireMinute
        )
        assert result == mockEmail + str(expireDate)

    def test_createRefreshToken(self, mockJWTService):
        result = mockJWTService.createRefreshToken(email=mockEmail)
        expireDate = mockJWTService.dateTimeNow() + timedelta(
            days=mockJWTService.refreshTokenExpireDay
        )
        assert result == mockEmail + str(expireDate)

    def test_checkTokenExpired_NOT_EXPIRE(self, mockJWTService):
        mockJWTService.now -= timedelta(minutes=100)
        result = mockJWTService.checkTokenExpired("")
        expectEmail = mockJWTService.decoder.decode("", "", "")["sub"]

        assert result == expectEmail

    def test_checkTokenExpired_EXPIRE(self, mockJWTService):
        result = mockJWTService.checkTokenExpired("")
        assert result == None
