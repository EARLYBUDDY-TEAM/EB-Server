from typing import Optional, TypeVar, List


K = TypeVar("K")
V = TypeVar("V")


# get method 사용하기
def safeDict(
    keyList: List[K],
    fromDict: Optional[dict],
) -> Optional[V]:
    try:
        if fromDict is None:
            return None
        if not keyList:
            return None
        tmpValue = fromDict[keyList[0]]
        for i in range(1, len(keyList)):
            tmpValue = tmpValue[keyList[i]]
        return tmpValue
    except:
        return None
