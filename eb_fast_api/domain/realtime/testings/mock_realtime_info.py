mock_real_time_json_to_real_time_info_dict = {
    "routeId": "755",
    "updownFlag": "2",
    "arrival2": {
        "fulCarAt": "0",
        "busPlateNo": "서울74사3829",
        "waitStatus": "1",
        "busStatus": "1",
        "endBusYn": "N",
        "leftStation": 7,
        "lowBusYn": "Y",
        "congestion": 1,
        "arrivalSec": 696,
        "nmprType": 4,
    },
    "localRouteId": "100100006",
    "arrival1": {
        "fulCarAt": "0",
        "busPlateNo": "서울71사1268",
        "waitStatus": "1",
        "busStatus": "1",
        "endBusYn": "N",
        "leftStation": 1,
        "lowBusYn": "Y",
        "congestion": 1,
        "arrivalSec": 130,
        "nmprType": 4,
    },
    "stationSeq": "32",
    "routeNm": "101",
}

mock_decode_real_time_info_list_dict = {
    "result": {
        "real": [mock_real_time_json_to_real_time_info_dict] * 5,
    }
}
