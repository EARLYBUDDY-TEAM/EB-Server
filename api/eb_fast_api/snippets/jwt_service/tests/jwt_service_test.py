import secrets
from eb_fast_api.snippets.jwt_service.sources.jwt_service import JWTEncoder


def test_JWT_Serialization_SUCCESS():
    # given
    jwtEncoder = JWTEncoder()
    algorithm = "HS256"
    secretKey = secrets.token_hex(32)
    testEmail = 'test@test.com'
    data = {'sub' : testEmail}
    expireDelta = 10

    # when, then
    try:
        token = jwtEncoder.encode(
            data=data,
            expireDelta=expireDelta,
            secretKey=secretKey,
            algorithm=algorithm,
        )



    except:
        raise Exception("fail test ...")


# def test_createToken():
