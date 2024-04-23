from sqlalchemy import Column, Integer, String

# from database.database import Base


# Path
from sys import path as sys_path
from pathlib import Path
here = Path(__file__)
print(here.as_uri)


# sys_path.append(here)
# from database import Base

# class User(Base):
#     __tablename__ = "Users"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)