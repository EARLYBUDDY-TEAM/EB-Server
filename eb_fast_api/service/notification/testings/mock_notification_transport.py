from unittest.mock import patch
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
)
from datetime import datetime


def patcher_init(
    return_value=None,
    side_effect=None,
):
    patcher = patch.object(
        NotificationTransport,
        "init",
        return_value=return_value,
        side_effect=side_effect,
    )

    return patcher


user_email = "abcd@abc.com"
schedule_id = "df5e3d53-937c-44f1-b297-b3b7bd612397"
schedule_name = "배차알림입니다"
schedule_time = datetime(2025, 2, 4, 16, 37, 36)
notify_transport = 10
notify_transport_range = 120
path_dict = {
    "type": 2,
    "time": 21,
    "walkTime": 6,
    "payment": 1500,
    "busTransitCount": 1,
    "subwayTransitCount": 0,
    "subPaths": [
        {
            "type": 3,
            "time": 2,
            "startName": "광화문역 5호선",
            "startX": "None",
            "startY": "None",
            "start_station_id": None,
            "way_code": None,
            "endName": "광화문",
            "distance": 158,
            "transports": [],
            "stations": [],
        },
        {
            "type": 2,
            "time": 15,
            "startName": "광화문",
            "startX": "126.976521",
            "startY": "37.570224",
            "start_station_id": 165600,
            "way_code": None,
            "endName": "동대문역.흥인지문",
            "distance": 3270,
            "transports": [
                {"subwayType": None, "busNumber": "370", "busType": "간선"},
                {"subwayType": None, "busNumber": "271", "busType": "간선"},
                {"subwayType": None, "busNumber": "721", "busType": "간선"},
                {"subwayType": None, "busNumber": "720", "busType": "간선"},
                {"subwayType": None, "busNumber": "270", "busType": "간선"},
                {"subwayType": None, "busNumber": "260", "busType": "간선"},
            ],
            "stations": [
                {"name": "광화문"},
                {"name": "종로1가"},
                {"name": "종로2가"},
                {"name": "종로3가.탑골공원"},
                {"name": "종로4가.종묘"},
                {"name": "종로5가.광장시장"},
                {"name": "종로6가.동대문종합시장"},
                {"name": "동대문역.흥인지문"},
            ],
        },
        {
            "type": 3,
            "time": 4,
            "startName": "동대문역.흥인지문",
            "startX": "None",
            "startY": "None",
            "start_station_id": None,
            "way_code": None,
            "endName": "동대문역 1호선",
            "distance": 299,
            "transports": [],
            "stations": [],
        },
    ],
}
now = datetime(2025, 2, 4, 15, 38, 23)
