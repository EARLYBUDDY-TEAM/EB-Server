from typing import Optional, TypeVar

K = TypeVar('K')
V = TypeVar('V')

def safeDict(keyList: [K], fromDict: dict) -> Optional[V]:
    try:
        if not keyList:
            return None
        tmpValue = fromDict[keyList[0]]
        for i in range(1, len(keyList)):
            tmpValue = tmpValue[keyList[i]]
        return tmpValue
    except:
        return None