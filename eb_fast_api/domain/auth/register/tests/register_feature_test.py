from eb_fast_api.domain.auth.register.sources import register_feature


def test_isValidEmail_SUCCESS():
    email = "abc@abc.com"
    try:
        register_feature.isValidEmail(email)
        return
    except:
        raise Exception("test fail")


def test_isValidEmail_FAIL():
    failEmailList = [
        "",
        "abc@"
        "abc@abc"
    ]

    for email in failEmailList:
        if register_feature.isValidEmail(email):
            raise Exception("test fail")


def test_isValidPassword_SUCCESS():
    password = "abcdefg12"
    try:
        register_feature.isValidPassword(password)
        return
    except:
        raise Exception("test fail")


def test_isValidPassword_FAIL():
    failPasswordList = [
        " ",
        "",
        "1",
        "1111111",
    ]

    for password in failPasswordList:
        if register_feature.isValidPassword(password):
            raise Exception("test fail")