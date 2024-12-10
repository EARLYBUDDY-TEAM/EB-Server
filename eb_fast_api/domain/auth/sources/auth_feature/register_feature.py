from email_validator import validate_email
from eb_fast_api.domain.schema.sources.schemas import RegisterInfo
from eb_fast_api.database.sources.crud.user_crud import UserCRUD


def createUser(
    registerInfo: RegisterInfo,
    userCRUD: UserCRUD,
):
    user = registerInfo.toUser()
    userCRUD.create(user)
    userCRUD.commit()


def isValidRegisterInfo(
    registerInfo: RegisterInfo,
) -> bool:
    return (
        False
        if not isValidEmail(registerInfo.email)
        or not isValidPassword(registerInfo.password)
        else True
    )


def isValidEmail(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=True)
        return True
    except:
        return False


def isValidPassword(password: str) -> bool:
    if " " in password or not password.strip():
        return False

    if len(password) < 6:
        return False

    digitFlag = False
    alphaFlag = False
    for p in password:
        if digitFlag and alphaFlag:
            break
        if p.isdigit():
            digitFlag = True
        elif p.isalpha():
            alphaFlag = True

    return digitFlag and alphaFlag
