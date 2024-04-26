from eb_server.domain.register.sources import register_feature

def test_is_valid_email_success():
    email = 'abc@abc.com'
    try:
        register_feature.is_valid_email(email)
        return
    except:
        raise Exception('test fail')

def test_is_valid_email_fail():
    email = ''
    try:
        register_feature.is_valid_email(email)
        raise Exception('test fail')
    except:
        return
    
def test_is_valid_password_success():
    password = 'abcdefg12'
    try:
        register_feature.is_valid_password(password)
        return
    except:
        raise Exception('test fail')
    
def test_is_valid_password_fail():
    password = ''
    try:
        register_feature.is_valid_password(password)
        raise Exception('test fail')
    except:
        return