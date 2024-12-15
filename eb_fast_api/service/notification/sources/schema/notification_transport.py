from datetime import datetime, timedelta
from typing import Optional, Self, List
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.snippets.sources import dictionary


class RequestRealTimeInfo:
    station_name: str
    dup: dict  # {버스번호 : 버스 번호판}, {transport_number : transport_plate}

    def __init__(
        self,
        station_name: str,
        dup: dict = dict(),
    ):
        self.station_name = station_name
        self.dup = dup

    @classmethod
    def mock(cls) -> Self:
        return cls(
            station_name="station_name",
            dup=dict(),
        )


class BusRequestRealTimeInfo(RequestRealTimeInfo):
    station_id: int

    def __init__(
        self,
        station_id: int,
        station_name: str,
        dup: dict = dict(),
    ):
        self.station_id = station_id
        self.station_name = station_name
        self.dup = dup

    @classmethod
    def mock(cls) -> Self:
        return cls(
            station_id=200,
            station_name="station_name",
        )

    def __eq__(self, other):
        if other == None:
            return False

        return self.station_id == other.station_id


class SubwayRequestRealTimeInfo(RequestRealTimeInfo):
    line_name: str
    direction: int

    def __init__(
        self,
        station_name: str,
        line_name: str,
        direction: int,
        dup: dict = dict(),
    ):
        self.station_name = station_name
        self.line_name = line_name
        self.direction = direction
        self.dup = dup

    @classmethod
    def mock(cls) -> Self:
        return cls(
            station_name="station_name",
            line_name="line_name",
            direction=1,
            dup=dict(),
        )

    def __eq__(self, other):
        if other == None:
            return False

        flag1 = self.station_name == other.station_name
        flag2 = self.line_name == other.line_name
        flag3 = self.direction == other.direction

        return flag1 and flag2 and flag3


class NotificationTransportContent:
    schedule_name: str
    arrival_before: int
    transport_type: str
    station_name: str

    def __init__(
        self,
        schedule_name: str,
        arrival_before: int,
        transport_type: str,
        station_name: str,
    ):
        self.schedule_name = schedule_name
        self.arrival_before = arrival_before
        self.transport_type = transport_type
        self.station_name = station_name

    @classmethod
    def mock(cls) -> Self:
        return cls(
            schedule_name="schedule_name",
            arrival_before=10,
            transport_type="버스",
            station_name="station_name",
        )


### 오늘 날짜 일정만 추가 ###
class NotificationTransport:
    schedule_id: str
    user_email: str
    noti_content: NotificationTransportContent
    noti_start_time: datetime  # only time
    noti_end_time: datetime  # only time
    request_realtime_info: RequestRealTimeInfo

    def __init__(
        self,
        schedule_id: str,
        user_email: str,
        noti_content: NotificationTransportContent,
        noti_start_time: datetime,
        noti_end_time: datetime,
        request_realtime_info: RequestRealTimeInfo,
    ):
        self.schedule_id = schedule_id
        self.user_email = user_email
        self.noti_content = noti_content
        self.noti_start_time = noti_start_time
        self.noti_end_time = noti_end_time
        self.request_realtime_info = request_realtime_info

    def __lt__(self, other):
        return self.noti_start_time < other.noti_start_time

    def __eq__(self, other):
        if other == None:
            return False

        return self.schedule_id == other.schedule_id

    @classmethod
    def get_request_real_time_info(
        cls,
        subpath_list: List[dict],
    ) -> Optional[RequestRealTimeInfo]:
        for subpath in subpath_list:
            try:
                type = subpath["type"]
                if type == 1:
                    return SubwayRequestRealTimeInfo(
                        station_name=subpath["startName"],
                        line_name=subpath["transports"][0]["subwayType"],
                        direction=subpath["way_code"],
                    )
                elif type == 2:
                    return BusRequestRealTimeInfo(
                        station_id=subpath["start_station_id"],
                        station_name=subpath["startName"],
                    )
                else:
                    continue
            except Exception as e:
                print(e)
                return None

    @classmethod
    def is_property_optional(
        cls,
        notify_transport: Optional[int],
        notify_transport_range: Optional[int],
        path_dict: Optional[dict],
    ) -> bool:
        return (
            notify_transport == None
            or notify_transport_range == None
            or path_dict == None
        )

    @classmethod
    def cal_noti_start_end_time(
        cls,
        schedule_time: datetime,
        notify_transport_range: Optional[int],
    ) -> Optional[tuple]:
        now = eb_datetime.get_datetime_now()

        if now.date() != schedule_time.date():
            print("not today")
            return None

        schedule_only_time = eb_datetime.get_only_time(schedule_time)
        now_time = eb_datetime.get_only_time(now)

        if schedule_only_time < now_time:
            print("schedule_only_time < now_time")
            return None

        noti_start_time = schedule_time - timedelta(minutes=notify_transport_range)
        noti_end_time = schedule_time
        noti_start_time = eb_datetime.get_only_time(noti_start_time)
        noti_end_time = eb_datetime.get_only_time(noti_end_time)
        return (noti_start_time, noti_end_time)

    @classmethod
    def create_request_real_time_info(
        cls,
        path_dict: dict,
    ) -> Optional[RequestRealTimeInfo]:
        subpath_list = dictionary.safeDict(["subPaths"], path_dict)
        if subpath_list == None:
            return None

        request_real_time_info = NotificationTransport.get_request_real_time_info(
            subpath_list=subpath_list,
        )

        return request_real_time_info

    @classmethod
    def init(
        cls,
        user_email: str,
        schedule_id: str,
        schedule_name: str,
        schedule_time: datetime,
        notify_transport: Optional[int],
        notify_transport_range: Optional[int],
        path_dict: Optional[dict],
    ) -> Optional[Self]:
        if cls.is_property_optional(
            notify_transport=notify_transport,
            notify_transport_range=notify_transport_range,
            path_dict=path_dict,
        ):
            return None

        noti_start_end_time = cls.cal_noti_start_end_time(
            schedule_time=schedule_time,
            notify_transport_range=notify_transport_range,
        )

        if noti_start_end_time == None:
            return None

        noti_start_time, noti_end_time = noti_start_end_time

        request_real_time_info = cls.create_request_real_time_info(
            path_dict=path_dict,
        )
        if request_real_time_info == None:
            return None

        isBus = isinstance(request_real_time_info, BusRequestRealTimeInfo)
        transport_type = "버스" if isBus else "지하철"

        noti_content = NotificationTransportContent(
            schedule_name=schedule_name,
            arrival_before=notify_transport,
            transport_type=transport_type,
            station_name=request_real_time_info.station_name,
        )

        return NotificationTransport(
            schedule_id=schedule_id,
            user_email=user_email,
            noti_content=noti_content,
            noti_start_time=noti_start_time,
            noti_end_time=noti_end_time,
            request_realtime_info=request_real_time_info,
        )

    @classmethod
    def mock_subway(cls) -> Self:
        return NotificationTransport(
            schedule_id="schedule_id",
            user_email="user_email",
            noti_content=NotificationTransportContent.mock(),
            noti_start_time=datetime.now().time(),
            noti_end_time=datetime.now().time(),
            request_realtime_info=SubwayRequestRealTimeInfo.mock(),
        )

    @classmethod
    def mock_bus(cls) -> Self:
        return NotificationTransport(
            schedule_id="schedule_id",
            user_email="user_email",
            noti_content=NotificationTransportContent.mock(),
            noti_start_time=datetime.now().time(),
            noti_end_time=datetime.now().time(),
            request_realtime_info=BusRequestRealTimeInfo.mock(),
        )