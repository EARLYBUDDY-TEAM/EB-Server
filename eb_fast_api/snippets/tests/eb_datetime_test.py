from datetime import datetime, timedelta
from eb_fast_api.snippets.sources import eb_datetime
from zoneinfo import ZoneInfo


def test_get_datetime_now():
    utc_now = datetime.now(ZoneInfo("Europe/London"))
    expect_now = utc_now + timedelta(hours=9)
    format = "%Y-%m-%d %H"
    expect_now = expect_now.strftime(format)
    now = eb_datetime.get_datetime_now().strftime(format)
    assert expect_now == now


def test_only_time():
    expect_now = datetime.now()
    expect_only_time = expect_now.time().replace(second=0, microsecond=0)
    only_time = eb_datetime.get_only_time(expect_now)
    assert expect_only_time == only_time
