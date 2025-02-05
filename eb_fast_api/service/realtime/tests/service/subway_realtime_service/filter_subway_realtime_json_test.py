from eb_fast_api.service.realtime.sources.service.subway_realtime_service.filter_subway_realtime_json import (
    filter_dup_realtime_arrival_list,
)
from eb_fast_api.service.realtime.testings.mock_subway_realtime_info import (
    mock_soosu,
)


def test_filter_dup_realtime_arrival_list():
    # given
    realtime_arrival_list = mock_soosu["realtimeArrivalList"]

    # when
    filtered_realtime_arrival_list = filter_dup_realtime_arrival_list(
        realtime_arrival_list=realtime_arrival_list
    )

    print(f"filtered_realtime_arrival_list : {filtered_realtime_arrival_list}")

    # then
    # assert filtered_realtime_arrival_list == []
