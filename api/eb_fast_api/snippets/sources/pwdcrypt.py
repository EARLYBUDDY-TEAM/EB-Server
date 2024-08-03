import bcrypt


salt = bcrypt.gensalt()


def check(password: str, hashedPassword: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashedPassword.encode(),
    )


def hash(password: str) -> str:
    passwordByte = password.encode()
    hashedPassword = bcrypt.hashpw(password=passwordByte, salt=salt)
    return hashedPassword.decode()
