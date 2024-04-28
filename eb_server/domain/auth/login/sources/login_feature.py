import bcrypt
from typing import Optional
from sqlalchemy.orm import Session

from eb_server.database.models import User

def get_user(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode(), hashed_password=hashed_password
    )