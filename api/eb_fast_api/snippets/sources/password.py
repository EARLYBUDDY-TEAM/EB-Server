import bcrypt


def check(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password.encode(),
    )


def hash(password: str) -> str:
    password_byte = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password_byte, salt=salt)
    return hashed_password.decode()
