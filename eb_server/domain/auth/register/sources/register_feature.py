from sqlalchemy.orm import Session
import bcrypt
from email_validator import validate_email

from eb_server.domain.auth.register.sources.register_schema import RegisterInfo
from eb_server.database.models import User

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

def is_exist_user(db: Session, register_info: RegisterInfo) -> bool:
    user = db.query(User).filter(User.email == register_info.email).first()
    return True if user != None else False

def create_user(db: Session, register_info: RegisterInfo):
    db_user = User(
        email=register_info.email,
        password=hash_password(register_info.password),
    )
    db.add(db_user)
    db.commit()

def hash_password(password: str) -> bytes:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password