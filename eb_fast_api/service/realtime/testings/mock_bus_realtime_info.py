from copy import deepcopy
from eb_fast_api.service.realtime.sources.realtime_service_schema import (
    ArrivalInfo,
    RealTimeInfo,
)

transport_number = "101"
arrival_sec1 = 130
arrival_sec2 = 696
left_station1 = 1
left_station2 = 7
transport_plate1 = "서울71사1268"
transport_plate2 = "서울74사3829"


mock_bus_arrival_json = {
    "fulCarAt": "0",
    "busPlateNo": transport_plate1,
    "waitStatus": "1",
    "busStatus": "1",
    "endBusYn": "N",
    "leftStation": left_station1,
    "lowBusYn": "Y",
    "congestion": 1,
    "arrivalSec": arrival_sec1,
    "nmprType": 4,
}


mock_bus_realtime_json = {
    "routeId": "755",
    "updownFlag": "2",
    "arrival2": {
        "fulCarAt": "0",
        "busPlateNo": transport_plate2,
        "waitStatus": "1",
        "busStatus": "1",
        "endBusYn": "N",
        "leftStation": left_station2,
        "lowBusYn": "Y",
        "congestion": 1,
        "arrivalSec": arrival_sec2,
        "nmprType": 4,
    },
    "arrival1": mock_bus_arrival_json,
    "stationSeq": "32",
    "routeNm": transport_number,
}


def mock_bus_decode_realtime_info_list_dict() -> dict:
    real = []

    for i in range(5):
        tmp_bus_realtime_json = deepcopy(mock_bus_realtime_json)
        tmp_bus_arrival_json = deepcopy(mock_bus_arrival_json)
        tmp_bus_arrival_json["arrivalSec"] -= i * 10
        tmp_bus_realtime_json["arrival1"] = tmp_bus_arrival_json
        real.append(tmp_bus_realtime_json)

    return {
        "result": {
            "real": real,
        }
    }


expected_arrival_info1 = ArrivalInfo(
    transport_plate=transport_plate1,
    arrival_sec=arrival_sec1,
    left_station=left_station1,
)

expected_arrival_info2 = ArrivalInfo(
    transport_plate=transport_plate2,
    arrival_sec=arrival_sec2,
    left_station=left_station2,
)

expected_realtime_info = RealTimeInfo(
    transport_number=transport_number,
    arrival_info1=expected_arrival_info1,
    arrival_info2=expected_arrival_info2,
)
