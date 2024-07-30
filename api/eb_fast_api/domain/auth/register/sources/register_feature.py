import bcrypt
from email_validator import validate_email


def is_valid_email(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=True)
        return True
    except:
        return False
    

def is_valid_password(password: str) -> bool:
    if password.strip():
        return True
    return False


def hash_password(password: str) -> bytes:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password