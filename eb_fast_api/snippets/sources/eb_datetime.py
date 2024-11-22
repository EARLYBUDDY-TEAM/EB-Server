from datetime import datetime, timezone, timedelta


KST = timezone(timedelta(hours=9))


def get_datetime_now() -> datetime:
    return datetime.now(KST).replace(tzinfo=None)
