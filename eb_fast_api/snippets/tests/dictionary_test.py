from eb_fast_api.snippets.sources import dictionary


def test_safeDict():
    keys = [1, 2, 3]
    myValue = "myValue"
    tmpDict = {1: {2: {3: myValue}}}
    try:
        tmpValue = dictionary.safeDict(keys, tmpDict)
        assert myValue == tmpValue
    except:
        raise Exception("find key, test fail")


def test_safeDict_from_dict_is_None():
    keys = [1, 2, 3]
    tmpDict = None
    try:
        tmpValue = dictionary.safeDict(keys, tmpDict)
        assert tmpValue == None
    except:
        raise Exception("find key, test fail")
