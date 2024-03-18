from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from database.models import User
import bcrypt

def create_user(db: Session, user_create: UserCreate):
    db_user = User(
        email = user_create.email,
        password = hash_password(user_create.password1),
        )
    db.add(db_user)
    db.commit()

# Hash a password using bcrypt
def hash_password(password: str) -> bytes:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password

# # Check if the provided password matches the stored password (hashed)
# def verify_password(plain_password, hashed_password):
#     password_byte_enc = plain_password.encode('utf-8')
#     return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)