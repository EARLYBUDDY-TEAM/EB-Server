from datetime import datetime, timezone, timedelta


KST_HOUR = 9
KST = timezone(timedelta(hours=KST_HOUR))


def get_datetime_now() -> datetime:
    return datetime.now(KST).replace(tzinfo=None, microsecond=0)


def get_only_time(dt: datetime) -> datetime:
    return dt.time().replace(second=0, microsecond=0)


def get_now_time() -> datetime:
    return get_only_time(get_datetime_now())
