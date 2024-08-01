import bcrypt
from email_validator import validate_email


def is_valid_email(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=True)
        return True
    except:
        return False
    

def is_valid_password(password: str) -> bool:
    if ' ' in password or not password.strip():
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