from eb_fast_api.database.sources.models import User, Schedule
from eb_fast_api.database.sources import db_crud


def test_user_create(mock_db):
    email = 'email'
    user = User(email = email, password = 'password')
    db_crud.user_create(user = user, db = mock_db)

    fetchedUser: User = db_crud.user_read(email = email, db = mock_db)
    
    print(user.email)
    print(fetchedUser.email)
    assert user.email == fetchedUser.email


def test_user_read():
    print('test_user_read')
    return