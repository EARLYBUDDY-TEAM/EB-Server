from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.domain.auth.sources.auth_feature.register_feature import isValidPassword


def update_pwd(
    email: str,
    password: str,
    user_crud: UserCRUD,
):
    hashed_password = pwdcrypt.hash(password)

    user_crud.update(
        key_email=email,
        hashedPassword=hashed_password,
    )

    user_crud.commit()
