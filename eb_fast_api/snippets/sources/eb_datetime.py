from datetime import datetime, timezone, timedelta


KST = timezone(timedelta(hours=9))


def get_datetime_now() -> datetime:
    return datetime.now(KST).replace(tzinfo=None)


def get_only_time(dt: datetime) -> datetime:
    return dt.time().replace(second=0, microsecond=0)
