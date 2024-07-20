# def test_is_valid_password_fail():
#     password = ''
#     try:
#         register_feature.is_valid_password(password)
#         raise Exception('test fail')
#     except:
#         return

from eb_fast_api.snippets.sources import snippets

def test_safeDict():
    keys = [1, 2, 3]
    myValue = 'myValue'
    tmpDict = {1 : {2 : {3 : myValue}}}
    try:
        tmpValue = snippets.safeDict(keys, tmpDict)
        assert myValue == tmpValue
    except:
        raise Exception('find key, test fail')