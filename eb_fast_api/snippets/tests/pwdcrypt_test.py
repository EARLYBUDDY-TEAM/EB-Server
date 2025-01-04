from eb_fast_api.snippets.sources import pwdcrypt


def test_hashAndCheck():
    pwd = "password123"
    hashedPwd = pwdcrypt.hash(pwd)

    return pwdcrypt.check(pwd, hashedPwd)
