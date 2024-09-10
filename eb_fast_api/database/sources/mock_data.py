from eb_fast_api.database.sources import crud
from eb_fast_api.database.sources.model import models
from eb_fast_api.database.sources import database
from eb_fast_api.snippets.sources import pwdcrypt


def testAccount(
    db: crud.CRUD,
    email="abc@abc.com",
    password="abcd12",
):
    hashedPassword = pwdcrypt.hash(password=password)
    user = models.User(
        email=email,
        hashedPassword=hashedPassword,
    )
    db.userCreate(user)
    db.commit()


def insertMockData():
    print("########## PREPARE MOCK DATA ##########")
    session = database.sessionMaker()
    db = crud.CRUD(session=session)
    print("Create Session")
    print("Create CRUD")

    testAccount(db)

    print("########## TEARDOWN DATABASE ##########")
    session.close()
    del db
    print("Close Session")
    print("DEL CRUD")


if __name__ == "__main__":
    insertMockData()
