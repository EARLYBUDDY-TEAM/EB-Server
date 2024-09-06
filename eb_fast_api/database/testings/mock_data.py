from eb_fast_api.database.sources.crud import CRUD, getDB
from eb_fast_api.database.sources.model import User
from eb_fast_api.snippets.sources import pwdcrypt
from typing import Annotated
from fastapi import Depends


def testAccount(
    db: CRUD,
    email="abc@abc.com",
    password="abcd12",
):
    hashedPassword = pwdcrypt.hash(password=password)
    user = User(
        email=email,
        hashedPassword=hashedPassword,
    )
    db.userCreate(user)
    db.commit()


# def insertMockData(database: Annotated[CRUD, Depends(getDB)]):
#     db = database()
