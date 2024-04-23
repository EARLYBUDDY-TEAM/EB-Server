# from sqlalchemy.orm import Session
# import bcrypt
# from typing import Optional
# from email_validator import validate_email

# # from domain.user.user_schema import UserCreate
# # from database.models import User


# # Path
# from sys import path as sys_path
# from pathlib import Path
# sys_path.append(Path(__file__).parent)
# from database import Base

# def is_valid_email(email: str) -> bool:
#     email_info = validate_email(email, check_deliverability=True)
#     return True

# def is_valid_password(password: str) -> bool:
#     if not password.strip():
#         return False
#     return True

# def create_user(db: Session, user_create: UserCreate):
#     db_user = User(
#         email=user_create.email,
#         password=hash_password(user_create.password),
#     )
#     db.add(db_user)
#     db.commit()

# # Hash a password using bcrypt
# def hash_password(password: str) -> bytes:
#     pwd_bytes = password.encode("utf-8")
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
#     return hashed_password

# # # Check if the provided password matches the stored password (hashed)
# # def verify_password(plain_password, hashed_password):
# #     password_byte_enc = plain_password.encode('utf-8')
# #     return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)

# def get_existing_user(db: Session, user_create: UserCreate) -> Optional[User]:
#     user = db.query(User).filter(User.email == user_create.email).first()
#     return user