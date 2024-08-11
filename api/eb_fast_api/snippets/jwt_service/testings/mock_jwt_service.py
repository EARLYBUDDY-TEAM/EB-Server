from eb_fast_api.snippets.jwt_service.interfaces.abs_jwt_serialization import ABSJWTDecoder, ABSJWTEncoder

# class MockJWTEncoder(ABSJWTEncoder):
#     def encode(
#         self, data: dict, expireDelta: int, secretKey: str, algorithm: str
#     ) -> str:
#         to_encode = data.copy()
#         expire = datetime.now(ZoneInfo("Asia/Seoul")) + timedelta(minutes=expireDelta)
#         to_encode.update({"exp": expire})
#         return jwt.encode(to_encode, secretKey, algorithm=algorithm)


# class MockJWTDecoder(ABSJWTDecoder):
#     def decode(self, token: str, secretKey: str, algorithm: str) -> dict | None:
#         try:
#             return jwt.decode(token, secretKey, algorithms=[algorithm])
#         except JWTError:
#             return None



