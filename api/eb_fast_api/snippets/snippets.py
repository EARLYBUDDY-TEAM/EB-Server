from typing import Optional

def getDataFromJson(k: str, j: dict) -> Optional[any]:
    try:
        return j[k]
    except:
        return None