from datetime import datetime, timedelta
from eb_fast_api.snippets.sources import eb_datetime


def test_get_datetime_now():
    expect_now = datetime.now() + timedelta(hours=9)
    format = "%Y-%m-%d %H"
    expect_now = expect_now.strftime(format)
    now = eb_datetime.get_datetime_now().strftime(format)
    assert expect_now == now
