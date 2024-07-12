from typing import Optional

def safeDict(k: any, j: dict) -> Optional[any]:
    try:
        return j[k]
    except:
        return None