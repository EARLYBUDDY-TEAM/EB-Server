from eb_server.domain.user.features import user_feature

def test_is_valid_email_success():
    email = 'abc@abc.com'
    try:
        user_feature.is_valid_email(email)
        return
    except:
        raise Exception('test fail')

def test_is_valid_email_fail():
    email = ''
    try:
        user_feature.is_valid_email(email)
        raise Exception('test fail')
    except:
        return
    
def test_is_valid_password_success():
    password = 'abcdefg12'
    try:
        user_feature.is_valid_password(password)
        return
    except:
        raise Exception('test fail')
    
def test_is_valid_password_fail():
    password = ''
    try:
        user_feature.is_valid_password(password)
        raise Exception('test fail')
    except:
        return