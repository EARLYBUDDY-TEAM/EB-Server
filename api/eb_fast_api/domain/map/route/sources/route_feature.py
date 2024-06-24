import httpx
from eb_fast_api.env.env import settings


async def getPTRouteData():
    url = 'https://api.odsay.com/v1/api/searchPubTransPathT'
    params = {
        'apiKey': settings.odsay,
        'SX': 127.10297988971773,
        'SY': 37.48800665367514,
        'EX': 126.994596,
        'EY': 37.534542,
        'OPT': 0
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, params=params)
        return response.json()

# 수서역 스타벅스 -> 이태원역
# {
#   "result": {
#     "searchType": 0,
#     "outTrafficCheck": 0,
#     "busCount": 10,
#     "subwayCount": 1,
#     "subwayBusCount": 5,
#     "pointDistance": 10886,
#     "startRadius": 700,
#     "endRadius": 700,
#     "path": [
#       {
#         "pathType": 1,
#         "info": {
#           "trafficDistance": 21800,
#           "totalWalk": 97,
#           "totalTime": 43,
#           "payment": 1600,
#           "busTransitCount": 0,
#           "subwayTransitCount": 2,
#           "mapObj": "3:2:349:333@6:2:633:630",
#           "firstStartStation": "수서",
#           "lastEndStation": "이태원",
#           "totalStationCount": 19,
#           "busStationCount": 0,
#           "subwayStationCount": 19,
#           "totalDistance": 21897,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 14
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 95,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 1,
#             "distance": 19100,
#             "sectionTime": 33,
#             "stationCount": 16,
#             "lane": [
#               {
#                 "name": "수도권 3호선",
#                 "subwayCode": 3,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 6,
#             "startName": "수서",
#             "startX": 127.102147,
#             "startY": 37.487473,
#             "endName": "약수",
#             "endX": 127.010997,
#             "endY": 37.554343,
#             "way": "약수",
#             "wayCode": 1,
#             "door": "4-3",
#             "startID": 349,
#             "endID": 333,
#             "startExitNo": "3",
#             "startExitX": 127.10232075621609,
#             "startExitY": 37.48778235566854,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 349,
#                   "stationName": "수서",
#                   "x": "127.102153",
#                   "y": "37.487477"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 348,
#                   "stationName": "일원",
#                   "x": "127.084225",
#                   "y": "37.484233"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 347,
#                   "stationName": "대청",
#                   "x": "127.079541",
#                   "y": "37.493608"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 346,
#                   "stationName": "학여울",
#                   "x": "127.071615",
#                   "y": "37.496712"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 345,
#                   "stationName": "대치",
#                   "x": "127.063442",
#                   "y": "37.494587"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 344,
#                   "stationName": "도곡",
#                   "x": "127.055349",
#                   "y": "37.490892"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 343,
#                   "stationName": "매봉",
#                   "x": "127.046921",
#                   "y": "37.487038"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 342,
#                   "stationName": "양재",
#                   "x": "127.034022",
#                   "y": "37.484557"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 341,
#                   "stationName": "남부터미널",
#                   "x": "127.016288",
#                   "y": "37.484917"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 340,
#                   "stationName": "교대",
#                   "x": "127.01382",
#                   "y": "37.493031"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 339,
#                   "stationName": "고속터미널",
#                   "x": "127.004975",
#                   "y": "37.504906"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 338,
#                   "stationName": "잠원",
#                   "x": "127.011629",
#                   "y": "37.512967"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 337,
#                   "stationName": "신사",
#                   "x": "127.020402",
#                   "y": "37.516484"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 336,
#                   "stationName": "압구정",
#                   "x": "127.028513",
#                   "y": "37.52633"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 335,
#                   "stationName": "옥수",
#                   "x": "127.017374",
#                   "y": "37.541609"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 334,
#                   "stationName": "금호",
#                   "x": "127.015801",
#                   "y": "37.548279"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 333,
#                   "stationName": "약수",
#                   "x": "127.011001",
#                   "y": "37.554347"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 1,
#             "distance": 2700,
#             "sectionTime": 8,
#             "stationCount": 3,
#             "lane": [
#               {
#                 "name": "수도권 6호선",
#                 "subwayCode": 6,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "약수",
#             "startX": 127.010298,
#             "startY": 37.554166,
#             "endName": "이태원",
#             "endX": 126.99458,
#             "endY": 37.534535,
#             "way": "이태원",
#             "wayCode": 1,
#             "door": "null",
#             "startID": 633,
#             "endID": 630,
#             "endExitNo": "2",
#             "endExitX": 126.99431246536089,
#             "endExitY": 37.53461171001717,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 633,
#                   "stationName": "약수",
#                   "x": "127.010306",
#                   "y": "37.554173"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 632,
#                   "stationName": "버티고개",
#                   "x": "127.00714",
#                   "y": "37.548111"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 631,
#                   "stationName": "한강진",
#                   "x": "127.001802",
#                   "y": "37.539829"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 630,
#                   "stationName": "이태원",
#                   "x": "126.99459",
#                   "y": "37.534542"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 2,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 14876,
#           "totalWalk": 773,
#           "totalTime": 59,
#           "payment": 1500,
#           "busTransitCount": 1,
#           "subwayTransitCount": 0,
#           "mapObj": "1048:1:13:40",
#           "firstStartStation": "수서역KT수서지점",
#           "lastEndStation": "용산구청",
#           "totalStationCount": 27,
#           "busStationCount": 27,
#           "subwayStationCount": 0,
#           "totalDistance": 15649,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 11
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 220,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 2,
#             "distance": 14876,
#             "sectionTime": 48,
#             "stationCount": 27,
#             "lane": [
#               {
#                 "busNo": "401",
#                 "type": 11,
#                 "busID": 1048,
#                 "busLocalBlID": "100100062",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역KT수서지점",
#             "startX": 127.100703,
#             "startY": 37.487219,
#             "endName": "용산구청",
#             "endX": 126.991231,
#             "endY": 37.530344,
#             "startID": 108946,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000297",
#             "startArsID": "23-404",
#             "endID": 105046,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000059",
#             "endArsID": "03-153",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108946,
#                   "stationName": "수서역KT수서지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000297",
#                   "arsID": "23-404",
#                   "x": "127.100703",
#                   "y": "37.487219",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108898,
#                   "stationName": "궁마을",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000299",
#                   "arsID": "23-406",
#                   "x": "127.097376",
#                   "y": "37.485518",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 151814,
#                   "stationName": "태화기독교.사회복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000348",
#                   "arsID": "23-465",
#                   "x": "127.093362",
#                   "y": "37.484577",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108750,
#                   "stationName": "수서삼성아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000276",
#                   "arsID": "23-380",
#                   "x": "127.091068",
#                   "y": "37.484469",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108577,
#                   "stationName": "일원본동주민센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000277",
#                   "arsID": "23-381",
#                   "x": "127.084691",
#                   "y": "37.483537",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 108491,
#                   "stationName": "푸른마을아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000278",
#                   "arsID": "23-382",
#                   "x": "127.080662",
#                   "y": "37.482947",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 108261,
#                   "stationName": "연금매점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000258",
#                   "arsID": "23-362",
#                   "x": "127.074565",
#                   "y": "37.488595",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 108196,
#                   "stationName": "대치아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000291",
#                   "arsID": "23-395",
#                   "x": "127.072482",
#                   "y": "37.49248",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 108077,
#                   "stationName": "쌍용아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000137",
#                   "arsID": "23-240",
#                   "x": "127.069425",
#                   "y": "37.498223",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 152000,
#                   "stationName": "새마을운동중앙회",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000388",
#                   "arsID": "23-511",
#                   "x": "127.067319",
#                   "y": "37.502081",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 107953,
#                   "stationName": "총회회관.휘문고입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000386",
#                   "arsID": "23-509",
#                   "x": "127.066012",
#                   "y": "37.504422",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 107875,
#                   "stationName": "삼성역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000139",
#                   "arsID": "23-242",
#                   "x": "127.064437",
#                   "y": "37.507356",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 107821,
#                   "stationName": "삼성역7번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000094",
#                   "arsID": "23-197",
#                   "x": "127.062736",
#                   "y": "37.510478",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107706,
#                   "stationName": "봉은사역3번출구.삼성1파출소",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000089",
#                   "arsID": "23-192",
#                   "x": "127.060143",
#                   "y": "37.515206",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107548,
#                   "stationName": "청담역.경기고교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000070",
#                   "arsID": "23-172",
#                   "x": "127.0561",
#                   "y": "37.520031",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107361,
#                   "stationName": "진흥아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000071",
#                   "arsID": "23-173",
#                   "x": "127.052014",
#                   "y": "37.519322",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 107147,
#                   "stationName": "강남구청.강남세무서",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000074",
#                   "arsID": "23-176",
#                   "x": "127.047262",
#                   "y": "37.518455",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 106845,
#                   "stationName": "청담동래미안아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000075",
#                   "arsID": "23-177",
#                   "x": "127.042793",
#                   "y": "37.51768",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 106780,
#                   "stationName": "강남구청역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000028",
#                   "arsID": "23-128",
#                   "x": "127.040041",
#                   "y": "37.517",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106581,
#                   "stationName": "세관앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000029",
#                   "arsID": "23-129",
#                   "x": "127.036063",
#                   "y": "37.515796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 106328,
#                   "stationName": "논현동사거리.학동역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000015",
#                   "arsID": "23-115",
#                   "x": "127.029596",
#                   "y": "37.513833",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106040,
#                   "stationName": "영동시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000016",
#                   "arsID": "23-116",
#                   "x": "127.023422",
#                   "y": "37.511872",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 105845,
#                   "stationName": "논현사거리.논현역5번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000107",
#                   "arsID": "22-183",
#                   "x": "127.019344",
#                   "y": "37.510631",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 105503,
#                   "stationName": "반포역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000017",
#                   "arsID": "22-017",
#                   "x": "127.012044",
#                   "y": "37.508354",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 105257,
#                   "stationName": "고속터미널",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000019",
#                   "arsID": "22-019",
#                   "x": "127.005228",
#                   "y": "37.506305",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 193940,
#                   "stationName": "반포대교남단.한강시민공원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000303",
#                   "arsID": "22-382",
#                   "x": "127.000309",
#                   "y": "37.507084",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 26,
#                   "stationID": 105058,
#                   "stationName": "한강중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000061",
#                   "arsID": "03-155",
#                   "x": "126.992478",
#                   "y": "37.525128",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 27,
#                   "stationID": 105046,
#                   "stationName": "용산구청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000059",
#                   "arsID": "03-153",
#                   "x": "126.991231",
#                   "y": "37.530344",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 553,
#             "sectionTime": 8
#           }
#         ]
#       },
#       {
#         "pathType": 3,
#         "info": {
#           "trafficDistance": 15550,
#           "totalWalk": 439,
#           "totalTime": 47,
#           "payment": 1700,
#           "busTransitCount": 1,
#           "subwayTransitCount": 1,
#           "mapObj": "3:2:349:342@1808:1:8:21",
#           "firstStartStation": "수서",
#           "lastEndStation": "이태원역.보광동입구",
#           "totalStationCount": 20,
#           "busStationCount": 13,
#           "subwayStationCount": 7,
#           "totalDistance": 15989,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 16
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 95,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 1,
#             "distance": 7500,
#             "sectionTime": 14,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "name": "수도권 3호선",
#                 "subwayCode": 3,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 6,
#             "startName": "수서",
#             "startX": 127.102147,
#             "startY": 37.487473,
#             "endName": "양재",
#             "endX": 127.034022,
#             "endY": 37.484549,
#             "way": "양재",
#             "wayCode": 1,
#             "door": "null",
#             "startID": 349,
#             "endID": 342,
#             "startExitNo": "3",
#             "startExitX": 127.10232075621609,
#             "startExitY": 37.48778235566854,
#             "endExitNo": "2",
#             "endExitX": 127.03353296720998,
#             "endExitY": 37.48501702352189,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 349,
#                   "stationName": "수서",
#                   "x": "127.102153",
#                   "y": "37.487477"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 348,
#                   "stationName": "일원",
#                   "x": "127.084225",
#                   "y": "37.484233"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 347,
#                   "stationName": "대청",
#                   "x": "127.079541",
#                   "y": "37.493608"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 346,
#                   "stationName": "학여울",
#                   "x": "127.071615",
#                   "y": "37.496712"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 345,
#                   "stationName": "대치",
#                   "x": "127.063442",
#                   "y": "37.494587"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 344,
#                   "stationName": "도곡",
#                   "x": "127.055349",
#                   "y": "37.490892"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 343,
#                   "stationName": "매봉",
#                   "x": "127.046921",
#                   "y": "37.487038"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 342,
#                   "stationName": "양재",
#                   "x": "127.034022",
#                   "y": "37.484557"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 256,
#             "sectionTime": 4
#           },
#           {
#             "trafficType": 2,
#             "distance": 8050,
#             "sectionTime": 27,
#             "stationCount": 13,
#             "lane": [
#               {
#                 "busNo": "421",
#                 "type": 11,
#                 "busID": 1808,
#                 "busLocalBlID": "100100409",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 10,
#             "startName": "뱅뱅사거리",
#             "startX": 127.032977,
#             "startY": 37.486703,
#             "endName": "이태원역.보광동입구",
#             "endX": 126.994251,
#             "endY": 37.533803,
#             "startID": 106410,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "121000006",
#             "startArsID": "22-006",
#             "endID": 105094,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000190",
#             "endArsID": "03-284",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 106410,
#                   "stationName": "뱅뱅사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000006",
#                   "arsID": "22-006",
#                   "x": "127.032977",
#                   "y": "37.486703",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 151879,
#                   "stationName": "순천향병원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000225",
#                   "arsID": "03-319",
#                   "x": "127.0067",
#                   "y": "37.532691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 151878,
#                   "stationName": "한남역.용산노인종합복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000191",
#                   "arsID": "03-285",
#                   "x": "127.00664",
#                   "y": "37.53124",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 193883,
#                   "stationName": "한남동하이페리온",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000230",
#                   "arsID": "03-324",
#                   "x": "127.005508",
#                   "y": "37.527915",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 166679,
#                   "stationName": "보광동신동아아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000183",
#                   "arsID": "03-277",
#                   "x": "127.001498",
#                   "y": "37.525691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 166680,
#                   "stationName": "기업은행보광동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000185",
#                   "arsID": "03-279",
#                   "x": "126.999386",
#                   "y": "37.527953",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 166682,
#                   "stationName": "한국폴리텍1대학",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000188",
#                   "arsID": "03-282",
#                   "x": "126.9965",
#                   "y": "37.530569",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 105094,
#                   "stationName": "이태원역.보광동입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000190",
#                   "arsID": "03-284",
#                   "x": "126.994251",
#                   "y": "37.533803",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 88,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 3,
#         "info": {
#           "trafficDistance": 15682,
#           "totalWalk": 457,
#           "totalTime": 48,
#           "payment": 1700,
#           "busTransitCount": 1,
#           "subwayTransitCount": 1,
#           "mapObj": "3:2:349:342@500:1:8:20",
#           "firstStartStation": "수서",
#           "lastEndStation": "이태원역.보광동 입구",
#           "totalStationCount": 19,
#           "busStationCount": 12,
#           "subwayStationCount": 7,
#           "totalDistance": 16139,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 18
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 95,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 1,
#             "distance": 7500,
#             "sectionTime": 14,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "name": "수도권 3호선",
#                 "subwayCode": 3,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 6,
#             "startName": "수서",
#             "startX": 127.102147,
#             "startY": 37.487473,
#             "endName": "양재",
#             "endX": 127.034022,
#             "endY": 37.484549,
#             "way": "양재",
#             "wayCode": 1,
#             "door": "null",
#             "startID": 349,
#             "endID": 342,
#             "startExitNo": "3",
#             "startExitX": 127.10232075621609,
#             "startExitY": 37.48778235566854,
#             "endExitNo": "2",
#             "endExitX": 127.03353296720998,
#             "endExitY": 37.48501702352189,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 349,
#                   "stationName": "수서",
#                   "x": "127.102153",
#                   "y": "37.487477"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 348,
#                   "stationName": "일원",
#                   "x": "127.084225",
#                   "y": "37.484233"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 347,
#                   "stationName": "대청",
#                   "x": "127.079541",
#                   "y": "37.493608"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 346,
#                   "stationName": "학여울",
#                   "x": "127.071615",
#                   "y": "37.496712"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 345,
#                   "stationName": "대치",
#                   "x": "127.063442",
#                   "y": "37.494587"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 344,
#                   "stationName": "도곡",
#                   "x": "127.055349",
#                   "y": "37.490892"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 343,
#                   "stationName": "매봉",
#                   "x": "127.046921",
#                   "y": "37.487038"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 342,
#                   "stationName": "양재",
#                   "x": "127.034022",
#                   "y": "37.484557"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 256,
#             "sectionTime": 4
#           },
#           {
#             "trafficType": 2,
#             "distance": 8182,
#             "sectionTime": 27,
#             "stationCount": 12,
#             "lane": [
#               {
#                 "busNo": "400",
#                 "type": 11,
#                 "busID": 500,
#                 "busLocalBlID": "100100596",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 12,
#             "startName": "뱅뱅사거리",
#             "startX": 127.032977,
#             "startY": 37.486703,
#             "endName": "이태원역.보광동 입구",
#             "endX": 126.994094,
#             "endY": 37.533675,
#             "startID": 106410,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "121000006",
#             "startArsID": "22-006",
#             "endID": 166805,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000189",
#             "endArsID": "03-283",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 106410,
#                   "stationName": "뱅뱅사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000006",
#                   "arsID": "22-006",
#                   "x": "127.032977",
#                   "y": "37.486703",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 166805,
#                   "stationName": "이태원역.보광동 입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000189",
#                   "arsID": "03-283",
#                   "x": "126.994094",
#                   "y": "37.533675",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 106,
#             "sectionTime": 2
#           }
#         ]
#       },
#       {
#         "pathType": 3,
#         "info": {
#           "trafficDistance": 21449,
#           "totalWalk": 577,
#           "totalTime": 54,
#           "payment": 1700,
#           "busTransitCount": 1,
#           "subwayTransitCount": 1,
#           "mapObj": "3:2:349:335@789:1:30:38",
#           "firstStartStation": "수서",
#           "lastEndStation": "이태원역1번출구.해밀턴호텔",
#           "totalStationCount": 22,
#           "busStationCount": 8,
#           "subwayStationCount": 14,
#           "totalDistance": 22026,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 14
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 95,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 1,
#             "distance": 17500,
#             "sectionTime": 30,
#             "stationCount": 14,
#             "lane": [
#               {
#                 "name": "수도권 3호선",
#                 "subwayCode": 3,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 6,
#             "startName": "수서",
#             "startX": 127.102147,
#             "startY": 37.487473,
#             "endName": "옥수",
#             "endX": 127.017366,
#             "endY": 37.541602,
#             "way": "옥수",
#             "wayCode": 1,
#             "door": "null",
#             "startID": 349,
#             "endID": 335,
#             "startExitNo": "3",
#             "startExitX": 127.10232075621609,
#             "startExitY": 37.48778235566854,
#             "endExitNo": "7",
#             "endExitX": 127.01696307637567,
#             "endExitY": 37.542585772637125,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 349,
#                   "stationName": "수서",
#                   "x": "127.102153",
#                   "y": "37.487477"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 348,
#                   "stationName": "일원",
#                   "x": "127.084225",
#                   "y": "37.484233"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 347,
#                   "stationName": "대청",
#                   "x": "127.079541",
#                   "y": "37.493608"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 346,
#                   "stationName": "학여울",
#                   "x": "127.071615",
#                   "y": "37.496712"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 345,
#                   "stationName": "대치",
#                   "x": "127.063442",
#                   "y": "37.494587"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 344,
#                   "stationName": "도곡",
#                   "x": "127.055349",
#                   "y": "37.490892"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 343,
#                   "stationName": "매봉",
#                   "x": "127.046921",
#                   "y": "37.487038"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 342,
#                   "stationName": "양재",
#                   "x": "127.034022",
#                   "y": "37.484557"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 341,
#                   "stationName": "남부터미널",
#                   "x": "127.016288",
#                   "y": "37.484917"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 340,
#                   "stationName": "교대",
#                   "x": "127.01382",
#                   "y": "37.493031"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 339,
#                   "stationName": "고속터미널",
#                   "x": "127.004975",
#                   "y": "37.504906"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 338,
#                   "stationName": "잠원",
#                   "x": "127.011629",
#                   "y": "37.512967"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 337,
#                   "stationName": "신사",
#                   "x": "127.020402",
#                   "y": "37.516484"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 336,
#                   "stationName": "압구정",
#                   "x": "127.028513",
#                   "y": "37.52633"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 335,
#                   "stationName": "옥수",
#                   "x": "127.017374",
#                   "y": "37.541609"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 346,
#             "sectionTime": 5
#           },
#           {
#             "trafficType": 2,
#             "distance": 3949,
#             "sectionTime": 16,
#             "stationCount": 8,
#             "lane": [
#               {
#                 "busNo": "110A",
#                 "type": 11,
#                 "busID": 789,
#                 "busLocalBlID": "100100016",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "옥수삼성아파트.래미안옥수리버젠",
#             "startX": 127.014632,
#             "startY": 37.543832,
#             "endName": "이태원역1번출구.해밀턴호텔",
#             "endX": 126.993052,
#             "endY": 37.534558,
#             "startID": 105644,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "103000063",
#             "startArsID": "04-162",
#             "endID": 105070,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000096",
#             "endArsID": "03-190",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105644,
#                   "stationName": "옥수삼성아파트.래미안옥수리버젠",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "103000063",
#                   "arsID": "04-162",
#                   "x": "127.014632",
#                   "y": "37.543832",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105459,
#                   "stationName": "옥정중학교입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "103000071",
#                   "arsID": "04-170",
#                   "x": "127.011005",
#                   "y": "37.540873",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105510,
#                   "stationName": "한남시범아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000116",
#                   "arsID": "03-210",
#                   "x": "127.012264",
#                   "y": "37.538027",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105381,
#                   "stationName": "한남동",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000118",
#                   "arsID": "03-212",
#                   "x": "127.008482",
#                   "y": "37.533986",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 105070,
#                   "stationName": "이태원역1번출구.해밀턴호텔",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000096",
#                   "arsID": "03-190",
#                   "x": "126.993052",
#                   "y": "37.534558",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 136,
#             "sectionTime": 2
#           }
#         ]
#       },
#       {
#         "pathType": 3,
#         "info": {
#           "trafficDistance": 16212,
#           "totalWalk": 293,
#           "totalTime": 56,
#           "payment": 1700,
#           "busTransitCount": 1,
#           "subwayTransitCount": 1,
#           "mapObj": "507:1:15:44@6:2:631:630",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원",
#           "totalStationCount": 30,
#           "busStationCount": 29,
#           "subwayStationCount": 1,
#           "totalDistance": 16505,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 19
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 15212,
#             "sectionTime": 49,
#             "stationCount": 29,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "서울시중부기술교육원.블루스퀘어",
#             "endX": 127.00318,
#             "endY": 37.541267,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 105254,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000067",
#             "endArsID": "03-161",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 107754,
#                   "stationName": "은마파출소",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000131",
#                   "arsID": "23-234",
#                   "x": "127.061521",
#                   "y": "37.498142",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 107700,
#                   "stationName": "대치현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000144",
#                   "arsID": "23-247",
#                   "x": "127.060039",
#                   "y": "37.500888",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 110411,
#                   "stationName": "대치사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000147",
#                   "arsID": "23-250",
#                   "x": "127.058579",
#                   "y": "37.50366",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 110413,
#                   "stationName": "포스코사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000099",
#                   "arsID": "23-202",
#                   "x": "127.056401",
#                   "y": "37.507788",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107482,
#                   "stationName": "한별구립어린이집",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000100",
#                   "arsID": "23-203",
#                   "x": "127.054885",
#                   "y": "37.510551",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107359,
#                   "stationName": "센트럴아이파크.강남구도시관리공단",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000101",
#                   "arsID": "23-204",
#                   "x": "127.052081",
#                   "y": "37.5158",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107147,
#                   "stationName": "강남구청.강남세무서",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000074",
#                   "arsID": "23-176",
#                   "x": "127.047262",
#                   "y": "37.518455",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 106845,
#                   "stationName": "청담동래미안아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000075",
#                   "arsID": "23-177",
#                   "x": "127.042793",
#                   "y": "37.51768",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 106821,
#                   "stationName": "강남구청역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000076",
#                   "arsID": "23-178",
#                   "x": "127.040938",
#                   "y": "37.518557",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 150804,
#                   "stationName": "영동고교앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000325",
#                   "arsID": "23-432",
#                   "x": "127.039847",
#                   "y": "37.52154",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106676,
#                   "stationName": "씨네시티.앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000059",
#                   "arsID": "23-161",
#                   "x": "127.037747",
#                   "y": "37.523018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 80000,
#                   "stationName": "도산공원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000651",
#                   "arsID": "23-155",
#                   "x": "127.034592",
#                   "y": "37.52202",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106477,
#                   "stationName": "도산공원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000060",
#                   "arsID": "23-162",
#                   "x": "127.033599",
#                   "y": "37.522732",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 106467,
#                   "stationName": "신구중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000061",
#                   "arsID": "23-163",
#                   "x": "127.033571",
#                   "y": "37.52576",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 106354,
#                   "stationName": "현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000048",
#                   "arsID": "23-148",
#                   "x": "127.03074",
#                   "y": "37.528584",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 106111,
#                   "stationName": "광림교회.현대고등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000004",
#                   "arsID": "23-104",
#                   "x": "127.02439",
#                   "y": "37.525342",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 105922,
#                   "stationName": "신사중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000002",
#                   "arsID": "23-102",
#                   "x": "127.021536",
#                   "y": "37.52385",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 26,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 27,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 28,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 29,
#                   "stationID": 105254,
#                   "stationName": "서울시중부기술교육원.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000067",
#                   "arsID": "03-161",
#                   "x": "127.00318",
#                   "y": "37.541267",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 202,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 1,
#             "distance": 1000,
#             "sectionTime": 2,
#             "stationCount": 1,
#             "lane": [
#               {
#                 "name": "수도권 6호선",
#                 "subwayCode": 6,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "한강진",
#             "startX": 127.001797,
#             "startY": 37.539822,
#             "endName": "이태원",
#             "endX": 126.99458,
#             "endY": 37.534535,
#             "way": "이태원",
#             "wayCode": 1,
#             "door": "null",
#             "startID": 631,
#             "endID": 630,
#             "startExitNo": "2",
#             "startExitX": 127.00203394837686,
#             "startExitY": 37.540706014622664,
#             "endExitNo": "2",
#             "endExitX": 126.99431246536089,
#             "endExitY": 37.53461171001717,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 631,
#                   "stationName": "한강진",
#                   "x": "127.001802",
#                   "y": "37.539829"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 630,
#                   "stationName": "이태원",
#                   "x": "126.99459",
#                   "y": "37.534542"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 2,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 3,
#         "info": {
#           "trafficDistance": 14851,
#           "totalWalk": 469,
#           "totalTime": 47,
#           "payment": 1600,
#           "busTransitCount": 1,
#           "subwayTransitCount": 2,
#           "mapObj": "116:2:1521:1513@7:2:730:732@1808:1:13:21",
#           "firstStartStation": "수서",
#           "lastEndStation": "이태원역.보광동입구",
#           "totalStationCount": 18,
#           "busStationCount": 8,
#           "subwayStationCount": 10,
#           "totalDistance": 15320,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 24
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 183,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 1,
#             "distance": 8000,
#             "sectionTime": 16,
#             "stationCount": 8,
#             "lane": [
#               {
#                 "name": "수도권 수인.분당선",
#                 "subwayCode": 116,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "수서",
#             "startX": 127.100909,
#             "startY": 37.487924,
#             "endName": "강남구청",
#             "endX": 127.041401,
#             "endY": 37.51684,
#             "way": "강남구청",
#             "wayCode": 1,
#             "door": "2-2",
#             "startID": 1521,
#             "endID": 1513,
#             "startExitNo": "3",
#             "startExitX": 127.10232075621609,
#             "startExitY": 37.48778235566854,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 1521,
#                   "stationName": "수서",
#                   "x": "127.100911",
#                   "y": "37.487927"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 1520,
#                   "stationName": "대모산입구",
#                   "x": "127.072761",
#                   "y": "37.491375"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 1519,
#                   "stationName": "개포동",
#                   "x": "127.066496",
#                   "y": "37.489182"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 1518,
#                   "stationName": "구룡",
#                   "x": "127.059345",
#                   "y": "37.487009"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 1517,
#                   "stationName": "도곡",
#                   "x": "127.055368",
#                   "y": "37.490994"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 1516,
#                   "stationName": "한티",
#                   "x": "127.052894",
#                   "y": "37.496215"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 1515,
#                   "stationName": "선릉",
#                   "x": "127.048606",
#                   "y": "37.505277"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 1514,
#                   "stationName": "선정릉",
#                   "x": "127.043642",
#                   "y": "37.510925"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 1513,
#                   "stationName": "강남구청",
#                   "x": "127.041404",
#                   "y": "37.516848"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 1,
#             "distance": 1900,
#             "sectionTime": 6,
#             "stationCount": 2,
#             "lane": [
#               {
#                 "name": "수도권 7호선",
#                 "subwayCode": 7,
#                 "subwayCityCode": 1000
#               }
#             ],
#             "intervalTime": 6,
#             "startName": "강남구청",
#             "startX": 127.041283,
#             "startY": 37.517181,
#             "endName": "논현",
#             "endX": 127.021351,
#             "endY": 37.511134,
#             "way": "논현",
#             "wayCode": 2,
#             "door": "null",
#             "startID": 730,
#             "endID": 732,
#             "endExitNo": "8",
#             "endExitX": 127.02086207228882,
#             "endExitY": 37.511625053528796,
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 730,
#                   "stationName": "강남구청",
#                   "x": "127.041289",
#                   "y": "37.517188"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 731,
#                   "stationName": "학동",
#                   "x": "127.031619",
#                   "y": "37.514251"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 732,
#                   "stationName": "논현",
#                   "x": "127.021356",
#                   "y": "37.511135"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 198,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 2,
#             "distance": 4951,
#             "sectionTime": 18,
#             "stationCount": 8,
#             "lane": [
#               {
#                 "busNo": "421",
#                 "type": 11,
#                 "busID": 1808,
#                 "busLocalBlID": "100100409",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 10,
#             "startName": "신사역",
#             "startX": 127.020661,
#             "startY": 37.512831,
#             "endName": "이태원역.보광동입구",
#             "endX": 126.994251,
#             "endY": 37.533803,
#             "startID": 105884,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "121000016",
#             "startArsID": "22-016",
#             "endID": 105094,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000190",
#             "endArsID": "03-284",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 151879,
#                   "stationName": "순천향병원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000225",
#                   "arsID": "03-319",
#                   "x": "127.0067",
#                   "y": "37.532691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 151878,
#                   "stationName": "한남역.용산노인종합복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000191",
#                   "arsID": "03-285",
#                   "x": "127.00664",
#                   "y": "37.53124",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 193883,
#                   "stationName": "한남동하이페리온",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000230",
#                   "arsID": "03-324",
#                   "x": "127.005508",
#                   "y": "37.527915",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 166679,
#                   "stationName": "보광동신동아아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000183",
#                   "arsID": "03-277",
#                   "x": "127.001498",
#                   "y": "37.525691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 166680,
#                   "stationName": "기업은행보광동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000185",
#                   "arsID": "03-279",
#                   "x": "126.999386",
#                   "y": "37.527953",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 166682,
#                   "stationName": "한국폴리텍1대학",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000188",
#                   "arsID": "03-282",
#                   "x": "126.9965",
#                   "y": "37.530569",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 105094,
#                   "stationName": "이태원역.보광동입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000190",
#                   "arsID": "03-284",
#                   "x": "126.994251",
#                   "y": "37.533803",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 88,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16148,
#           "totalWalk": 271,
#           "totalTime": 61,
#           "payment": 1700,
#           "busTransitCount": 2,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:43@789:1:34:37",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원119안전센터",
#           "totalStationCount": 31,
#           "busStationCount": 31,
#           "subwayStationCount": 0,
#           "totalDistance": 16419,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 19
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 14383,
#             "sectionTime": 47,
#             "stationCount": 28,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "순천향대학병원",
#             "endX": 127.00578,
#             "endY": 37.536396,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 105318,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000068",
#             "endArsID": "03-162",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 107754,
#                   "stationName": "은마파출소",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000131",
#                   "arsID": "23-234",
#                   "x": "127.061521",
#                   "y": "37.498142",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 107700,
#                   "stationName": "대치현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000144",
#                   "arsID": "23-247",
#                   "x": "127.060039",
#                   "y": "37.500888",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 110411,
#                   "stationName": "대치사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000147",
#                   "arsID": "23-250",
#                   "x": "127.058579",
#                   "y": "37.50366",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 110413,
#                   "stationName": "포스코사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000099",
#                   "arsID": "23-202",
#                   "x": "127.056401",
#                   "y": "37.507788",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107482,
#                   "stationName": "한별구립어린이집",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000100",
#                   "arsID": "23-203",
#                   "x": "127.054885",
#                   "y": "37.510551",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107359,
#                   "stationName": "센트럴아이파크.강남구도시관리공단",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000101",
#                   "arsID": "23-204",
#                   "x": "127.052081",
#                   "y": "37.5158",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107147,
#                   "stationName": "강남구청.강남세무서",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000074",
#                   "arsID": "23-176",
#                   "x": "127.047262",
#                   "y": "37.518455",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 106845,
#                   "stationName": "청담동래미안아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000075",
#                   "arsID": "23-177",
#                   "x": "127.042793",
#                   "y": "37.51768",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 106821,
#                   "stationName": "강남구청역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000076",
#                   "arsID": "23-178",
#                   "x": "127.040938",
#                   "y": "37.518557",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 150804,
#                   "stationName": "영동고교앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000325",
#                   "arsID": "23-432",
#                   "x": "127.039847",
#                   "y": "37.52154",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106676,
#                   "stationName": "씨네시티.앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000059",
#                   "arsID": "23-161",
#                   "x": "127.037747",
#                   "y": "37.523018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 80000,
#                   "stationName": "도산공원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000651",
#                   "arsID": "23-155",
#                   "x": "127.034592",
#                   "y": "37.52202",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106477,
#                   "stationName": "도산공원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000060",
#                   "arsID": "23-162",
#                   "x": "127.033599",
#                   "y": "37.522732",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 106467,
#                   "stationName": "신구중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000061",
#                   "arsID": "23-163",
#                   "x": "127.033571",
#                   "y": "37.52576",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 106354,
#                   "stationName": "현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000048",
#                   "arsID": "23-148",
#                   "x": "127.03074",
#                   "y": "37.528584",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 106111,
#                   "stationName": "광림교회.현대고등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000004",
#                   "arsID": "23-104",
#                   "x": "127.02439",
#                   "y": "37.525342",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 105922,
#                   "stationName": "신사중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000002",
#                   "arsID": "23-102",
#                   "x": "127.021536",
#                   "y": "37.52385",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 26,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 27,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 28,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 1765,
#             "sectionTime": 10,
#             "stationCount": 3,
#             "lane": [
#               {
#                 "busNo": "110A",
#                 "type": 11,
#                 "busID": 789,
#                 "busLocalBlID": "100100016",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               },
#               {
#                 "busNo": "400",
#                 "type": 11,
#                 "busID": 500,
#                 "busLocalBlID": "100100596",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "순천향대학병원",
#             "startX": 127.00578,
#             "startY": 37.536396,
#             "endName": "이태원119안전센터",
#             "endX": 126.996625,
#             "endY": 37.534796,
#             "startID": 105318,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000068",
#             "startArsID": "03-162",
#             "endID": 105152,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000098",
#             "endArsID": "03-192",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 182,
#             "sectionTime": 3
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 15062,
#           "totalWalk": 773,
#           "totalTime": 64,
#           "payment": 1700,
#           "busTransitCount": 2,
#           "subwayTransitCount": 0,
#           "mapObj": "1062:1:11:36@872:1:81:84",
#           "firstStartStation": "수서역KT수서지점",
#           "lastEndStation": "용산구청",
#           "totalStationCount": 28,
#           "busStationCount": 28,
#           "subwayStationCount": 0,
#           "totalDistance": 15835,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 18
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 220,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 2,
#             "distance": 11744,
#             "sectionTime": 40,
#             "stationCount": 25,
#             "lane": [
#               {
#                 "busNo": "361",
#                 "type": 11,
#                 "busID": 1062,
#                 "busLocalBlID": "100100454",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역KT수서지점",
#             "startX": 127.100703,
#             "startY": 37.487219,
#             "endName": "고속터미널",
#             "endX": 127.005228,
#             "endY": 37.506305,
#             "startID": 108946,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000297",
#             "startArsID": "23-404",
#             "endID": 105257,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "121000019",
#             "endArsID": "22-019",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108946,
#                   "stationName": "수서역KT수서지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000297",
#                   "arsID": "23-404",
#                   "x": "127.100703",
#                   "y": "37.487219",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108898,
#                   "stationName": "궁마을",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000299",
#                   "arsID": "23-406",
#                   "x": "127.097376",
#                   "y": "37.485518",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 151814,
#                   "stationName": "태화기독교.사회복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000348",
#                   "arsID": "23-465",
#                   "x": "127.093362",
#                   "y": "37.484577",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108750,
#                   "stationName": "수서삼성아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000276",
#                   "arsID": "23-380",
#                   "x": "127.091068",
#                   "y": "37.484469",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108577,
#                   "stationName": "일원본동주민센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000277",
#                   "arsID": "23-381",
#                   "x": "127.084691",
#                   "y": "37.483537",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 108491,
#                   "stationName": "푸른마을아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000278",
#                   "arsID": "23-382",
#                   "x": "127.080662",
#                   "y": "37.482947",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 108261,
#                   "stationName": "연금매점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000258",
#                   "arsID": "23-362",
#                   "x": "127.074565",
#                   "y": "37.488595",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 108196,
#                   "stationName": "대치아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000291",
#                   "arsID": "23-395",
#                   "x": "127.072482",
#                   "y": "37.49248",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 108077,
#                   "stationName": "쌍용아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000137",
#                   "arsID": "23-240",
#                   "x": "127.069425",
#                   "y": "37.498223",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 107825,
#                   "stationName": "래미안하이스턴.대치순복음교회",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000143",
#                   "arsID": "23-246",
#                   "x": "127.063704",
#                   "y": "37.499916",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 107698,
#                   "stationName": "은마아파트입구사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000160",
#                   "arsID": "23-263",
#                   "x": "127.059987",
#                   "y": "37.498752",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 111822,
#                   "stationName": "도곡초등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000161",
#                   "arsID": "23-264",
#                   "x": "127.056653",
#                   "y": "37.497653",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 107453,
#                   "stationName": "한티역2번출구.서울강남고용노동지청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000162",
#                   "arsID": "23-265",
#                   "x": "127.053893",
#                   "y": "37.496784",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107345,
#                   "stationName": "한티역7번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000206",
#                   "arsID": "23-310",
#                   "x": "127.051494",
#                   "y": "37.496044",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107185,
#                   "stationName": "역삼중학교.강남세브란스병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000207",
#                   "arsID": "23-311",
#                   "x": "127.047621",
#                   "y": "37.494652",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107092,
#                   "stationName": "역삼2동주민센터.대림역삼아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000192",
#                   "arsID": "23-296",
#                   "x": "127.045972",
#                   "y": "37.49627",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 106992,
#                   "stationName": "역삼자이아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000194",
#                   "arsID": "23-298",
#                   "x": "127.044321",
#                   "y": "37.499797",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 106873,
#                   "stationName": "KT강남지사",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000175",
#                   "arsID": "23-278",
#                   "x": "127.042019",
#                   "y": "37.504717",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 106666,
#                   "stationName": "국민은행논현동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000043",
#                   "arsID": "23-143",
#                   "x": "127.037446",
#                   "y": "37.508536",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106515,
#                   "stationName": "언주역4번출구.차병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000044",
#                   "arsID": "23-144",
#                   "x": "127.034674",
#                   "y": "37.507712",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 106379,
#                   "stationName": "삼정호텔",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000020",
#                   "arsID": "23-120",
#                   "x": "127.031643",
#                   "y": "37.506813",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106235,
#                   "stationName": "신논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000021",
#                   "arsID": "23-121",
#                   "x": "127.026044",
#                   "y": "37.505109",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 105845,
#                   "stationName": "논현사거리.논현역5번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000107",
#                   "arsID": "22-183",
#                   "x": "127.019344",
#                   "y": "37.510631",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 105503,
#                   "stationName": "반포역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000017",
#                   "arsID": "22-017",
#                   "x": "127.012044",
#                   "y": "37.508354",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 105257,
#                   "stationName": "고속터미널",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000019",
#                   "arsID": "22-019",
#                   "x": "127.005228",
#                   "y": "37.506305",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 3318,
#             "sectionTime": 13,
#             "stationCount": 3,
#             "lane": [
#               {
#                 "busNo": "143",
#                 "type": 11,
#                 "busID": 872,
#                 "busLocalBlID": "100100022",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 7,
#             "startName": "고속터미널",
#             "startX": 127.005228,
#             "startY": 37.506305,
#             "endName": "용산구청",
#             "endX": 126.991231,
#             "endY": 37.530344,
#             "startID": 105257,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "121000019",
#             "startArsID": "22-019",
#             "endID": 105046,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000059",
#             "endArsID": "03-153",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105257,
#                   "stationName": "고속터미널",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000019",
#                   "arsID": "22-019",
#                   "x": "127.005228",
#                   "y": "37.506305",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 193940,
#                   "stationName": "반포대교남단.한강시민공원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000303",
#                   "arsID": "22-382",
#                   "x": "127.000309",
#                   "y": "37.507084",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105058,
#                   "stationName": "한강중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000061",
#                   "arsID": "03-155",
#                   "x": "126.992478",
#                   "y": "37.525128",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105046,
#                   "stationName": "용산구청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000059",
#                   "arsID": "03-153",
#                   "x": "126.991231",
#                   "y": "37.530344",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 553,
#             "sectionTime": 8
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16794,
#           "totalWalk": 402,
#           "totalTime": 65,
#           "payment": 1700,
#           "busTransitCount": 2,
#           "subwayTransitCount": 0,
#           "mapObj": "1050:1:13:41@789:1:34:37",
#           "firstStartStation": "수서역KT수서지점",
#           "lastEndStation": "이태원119안전센터",
#           "totalStationCount": 31,
#           "busStationCount": 31,
#           "subwayStationCount": 0,
#           "totalDistance": 17196,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 17
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 220,
#             "sectionTime": 3
#           },
#           {
#             "trafficType": 2,
#             "distance": 15029,
#             "sectionTime": 49,
#             "stationCount": 28,
#             "lane": [
#               {
#                 "busNo": "402",
#                 "type": 11,
#                 "busID": 1050,
#                 "busLocalBlID": "100100063",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "수서역KT수서지점",
#             "startX": 127.100703,
#             "startY": 37.487219,
#             "endName": "순천향대학병원",
#             "endX": 127.00578,
#             "endY": 37.536396,
#             "startID": 108946,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000297",
#             "startArsID": "23-404",
#             "endID": 105318,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000068",
#             "endArsID": "03-162",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108946,
#                   "stationName": "수서역KT수서지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000297",
#                   "arsID": "23-404",
#                   "x": "127.100703",
#                   "y": "37.487219",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108898,
#                   "stationName": "궁마을",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000299",
#                   "arsID": "23-406",
#                   "x": "127.097376",
#                   "y": "37.485518",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 151814,
#                   "stationName": "태화기독교.사회복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000348",
#                   "arsID": "23-465",
#                   "x": "127.093362",
#                   "y": "37.484577",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108750,
#                   "stationName": "수서삼성아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000276",
#                   "arsID": "23-380",
#                   "x": "127.091068",
#                   "y": "37.484469",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108577,
#                   "stationName": "일원본동주민센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000277",
#                   "arsID": "23-381",
#                   "x": "127.084691",
#                   "y": "37.483537",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 108491,
#                   "stationName": "푸른마을아파트앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000278",
#                   "arsID": "23-382",
#                   "x": "127.080662",
#                   "y": "37.482947",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 108038,
#                   "stationName": "개포시장.개포5단지상가",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000252",
#                   "arsID": "23-356",
#                   "x": "127.068382",
#                   "y": "37.489375",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 111768,
#                   "stationName": "개포6단지앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000254",
#                   "arsID": "23-358",
#                   "x": "127.07041",
#                   "y": "37.48995",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 108196,
#                   "stationName": "대치아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000291",
#                   "arsID": "23-395",
#                   "x": "127.072482",
#                   "y": "37.49248",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 107965,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000134",
#                   "arsID": "23-237",
#                   "x": "127.067035",
#                   "y": "37.495816",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107769,
#                   "stationName": "대치역1번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000123",
#                   "arsID": "23-226",
#                   "x": "127.061607",
#                   "y": "37.493971",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107676,
#                   "stationName": "래미안.대치.팰리스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000124",
#                   "arsID": "23-227",
#                   "x": "127.058436",
#                   "y": "37.492513",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107569,
#                   "stationName": "도곡역2번출구.동부센트레빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000116",
#                   "arsID": "23-219",
#                   "x": "127.056716",
#                   "y": "37.491724",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 107363,
#                   "stationName": "숙명여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000225",
#                   "arsID": "23-329",
#                   "x": "127.052511",
#                   "y": "37.489826",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 107230,
#                   "stationName": "매봉삼성아파트SK리더스뷰",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000212",
#                   "arsID": "23-316",
#                   "x": "127.048868",
#                   "y": "37.488192",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 193747,
#                   "stationName": "매봉역양재최의원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000213",
#                   "arsID": "23-317",
#                   "x": "127.044482",
#                   "y": "37.486247",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106616,
#                   "stationName": "양재역말죽거리.강남베드로병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000214",
#                   "arsID": "23-318",
#                   "x": "127.037891",
#                   "y": "37.485256",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 106410,
#                   "stationName": "뱅뱅사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000006",
#                   "arsID": "22-006",
#                   "x": "127.032977",
#                   "y": "37.486703",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 26,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 27,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 28,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 1765,
#             "sectionTime": 10,
#             "stationCount": 3,
#             "lane": [
#               {
#                 "busNo": "110A",
#                 "type": 11,
#                 "busID": 789,
#                 "busLocalBlID": "100100016",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               },
#               {
#                 "busNo": "400",
#                 "type": 11,
#                 "busID": 500,
#                 "busLocalBlID": "100100596",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "순천향대학병원",
#             "startX": 127.00578,
#             "startY": 37.536396,
#             "endName": "이태원119안전센터",
#             "endX": 126.996625,
#             "endY": 37.534796,
#             "startID": 105318,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000068",
#             "startArsID": "03-162",
#             "endID": 105152,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000098",
#             "endArsID": "03-192",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 182,
#             "sectionTime": 3
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16157,
#           "totalWalk": 320,
#           "totalTime": 62,
#           "payment": 1700,
#           "busTransitCount": 2,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:42@1808:1:15:21",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역.보광동입구",
#           "totalStationCount": 33,
#           "busStationCount": 33,
#           "subwayStationCount": 0,
#           "totalDistance": 16477,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 21
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 13942,
#             "sectionTime": 46,
#             "stationCount": 27,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "한남5거리",
#             "endX": 127.008281,
#             "endY": 37.532957,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 105378,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000072",
#             "endArsID": "03-166",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 107754,
#                   "stationName": "은마파출소",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000131",
#                   "arsID": "23-234",
#                   "x": "127.061521",
#                   "y": "37.498142",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 107700,
#                   "stationName": "대치현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000144",
#                   "arsID": "23-247",
#                   "x": "127.060039",
#                   "y": "37.500888",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 110411,
#                   "stationName": "대치사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000147",
#                   "arsID": "23-250",
#                   "x": "127.058579",
#                   "y": "37.50366",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 110413,
#                   "stationName": "포스코사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000099",
#                   "arsID": "23-202",
#                   "x": "127.056401",
#                   "y": "37.507788",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 107482,
#                   "stationName": "한별구립어린이집",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000100",
#                   "arsID": "23-203",
#                   "x": "127.054885",
#                   "y": "37.510551",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 107359,
#                   "stationName": "센트럴아이파크.강남구도시관리공단",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000101",
#                   "arsID": "23-204",
#                   "x": "127.052081",
#                   "y": "37.5158",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 107147,
#                   "stationName": "강남구청.강남세무서",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000074",
#                   "arsID": "23-176",
#                   "x": "127.047262",
#                   "y": "37.518455",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 106845,
#                   "stationName": "청담동래미안아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000075",
#                   "arsID": "23-177",
#                   "x": "127.042793",
#                   "y": "37.51768",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 106821,
#                   "stationName": "강남구청역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000076",
#                   "arsID": "23-178",
#                   "x": "127.040938",
#                   "y": "37.518557",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 18,
#                   "stationID": 150804,
#                   "stationName": "영동고교앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000325",
#                   "arsID": "23-432",
#                   "x": "127.039847",
#                   "y": "37.52154",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 19,
#                   "stationID": 106676,
#                   "stationName": "씨네시티.앞",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000059",
#                   "arsID": "23-161",
#                   "x": "127.037747",
#                   "y": "37.523018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 20,
#                   "stationID": 80000,
#                   "stationName": "도산공원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000651",
#                   "arsID": "23-155",
#                   "x": "127.034592",
#                   "y": "37.52202",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 21,
#                   "stationID": 106477,
#                   "stationName": "도산공원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000060",
#                   "arsID": "23-162",
#                   "x": "127.033599",
#                   "y": "37.522732",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 22,
#                   "stationID": 106467,
#                   "stationName": "신구중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000061",
#                   "arsID": "23-163",
#                   "x": "127.033571",
#                   "y": "37.52576",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 23,
#                   "stationID": 106354,
#                   "stationName": "현대아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000048",
#                   "arsID": "23-148",
#                   "x": "127.03074",
#                   "y": "37.528584",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 24,
#                   "stationID": 106111,
#                   "stationName": "광림교회.현대고등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000004",
#                   "arsID": "23-104",
#                   "x": "127.02439",
#                   "y": "37.525342",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 25,
#                   "stationID": 105922,
#                   "stationName": "신사중학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000002",
#                   "arsID": "23-102",
#                   "x": "127.021536",
#                   "y": "37.52385",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 26,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 27,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 143,
#             "sectionTime": 2
#           },
#           {
#             "trafficType": 2,
#             "distance": 2215,
#             "sectionTime": 12,
#             "stationCount": 6,
#             "lane": [
#               {
#                 "busNo": "421",
#                 "type": 11,
#                 "busID": 1808,
#                 "busLocalBlID": "100100409",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 10,
#             "startName": "순천향병원입구",
#             "startX": 127.0067,
#             "startY": 37.532691,
#             "endName": "이태원역.보광동입구",
#             "endX": 126.994251,
#             "endY": 37.533803,
#             "startID": 151879,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000225",
#             "startArsID": "03-319",
#             "endID": 105094,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000190",
#             "endArsID": "03-284",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 151879,
#                   "stationName": "순천향병원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000225",
#                   "arsID": "03-319",
#                   "x": "127.0067",
#                   "y": "37.532691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 151878,
#                   "stationName": "한남역.용산노인종합복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000191",
#                   "arsID": "03-285",
#                   "x": "127.00664",
#                   "y": "37.53124",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 193883,
#                   "stationName": "한남동하이페리온",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000230",
#                   "arsID": "03-324",
#                   "x": "127.005508",
#                   "y": "37.527915",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 166679,
#                   "stationName": "보광동신동아아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000183",
#                   "arsID": "03-277",
#                   "x": "127.001498",
#                   "y": "37.525691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 166680,
#                   "stationName": "기업은행보광동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000185",
#                   "arsID": "03-279",
#                   "x": "126.999386",
#                   "y": "37.527953",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 166682,
#                   "stationName": "한국폴리텍1대학",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000188",
#                   "arsID": "03-282",
#                   "x": "126.9965",
#                   "y": "37.530569",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 105094,
#                   "stationName": "이태원역.보광동입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000190",
#                   "arsID": "03-284",
#                   "x": "126.994251",
#                   "y": "37.533803",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 88,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16295,
#           "totalWalk": 225,
#           "totalTime": 63,
#           "payment": 1700,
#           "busTransitCount": 3,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:22@1054:1:3:20@789:1:34:38",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역1번출구.해밀턴호텔",
#           "totalStationCount": 28,
#           "busStationCount": 28,
#           "subwayStationCount": 0,
#           "totalDistance": 16520,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 28
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 4965,
#             "sectionTime": 18,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "대치역6번출구.강남구민회관",
#             "endX": 127.064291,
#             "endY": 37.492776,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 107873,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000136",
#             "endArsID": "23-239",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 9248,
#             "sectionTime": 31,
#             "stationCount": 17,
#             "lane": [
#               {
#                 "busNo": "420",
#                 "type": 11,
#                 "busID": 1054,
#                 "busLocalBlID": "100100068",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "대치역6번출구.강남구민회관",
#             "startX": 127.064291,
#             "startY": 37.492776,
#             "endName": "순천향대학병원",
#             "endX": 127.00578,
#             "endY": 37.536396,
#             "startID": 107873,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000136",
#             "startArsID": "23-239",
#             "endID": 105318,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000068",
#             "endArsID": "03-162",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 107698,
#                   "stationName": "은마아파트입구사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000160",
#                   "arsID": "23-263",
#                   "x": "127.059987",
#                   "y": "37.498752",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 111822,
#                   "stationName": "도곡초등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000161",
#                   "arsID": "23-264",
#                   "x": "127.056653",
#                   "y": "37.497653",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 107453,
#                   "stationName": "한티역2번출구.서울강남고용노동지청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000162",
#                   "arsID": "23-265",
#                   "x": "127.053893",
#                   "y": "37.496784",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107345,
#                   "stationName": "한티역7번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000206",
#                   "arsID": "23-310",
#                   "x": "127.051494",
#                   "y": "37.496044",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107185,
#                   "stationName": "역삼중학교.강남세브란스병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000207",
#                   "arsID": "23-311",
#                   "x": "127.047621",
#                   "y": "37.494652",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 106871,
#                   "stationName": "도곡1차아이파크.역삼청소년수련관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000208",
#                   "arsID": "23-312",
#                   "x": "127.041809",
#                   "y": "37.492848",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 106703,
#                   "stationName": "역삼럭키아파트.역삼월드메르디앙아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000187",
#                   "arsID": "23-291",
#                   "x": "127.038677",
#                   "y": "37.491886",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 106435,
#                   "stationName": "뱅뱅사거리.역삼동",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000190",
#                   "arsID": "23-294",
#                   "x": "127.033721",
#                   "y": "37.490349",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 16,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 17,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 2082,
#             "sectionTime": 11,
#             "stationCount": 4,
#             "lane": [
#               {
#                 "busNo": "110A",
#                 "type": 11,
#                 "busID": 789,
#                 "busLocalBlID": "100100016",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "순천향대학병원",
#             "startX": 127.00578,
#             "startY": 37.536396,
#             "endName": "이태원역1번출구.해밀턴호텔",
#             "endX": 126.993052,
#             "endY": 37.534558,
#             "startID": 105318,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000068",
#             "startArsID": "03-162",
#             "endID": 105070,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000096",
#             "endArsID": "03-190",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105070,
#                   "stationName": "이태원역1번출구.해밀턴호텔",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000096",
#                   "arsID": "03-190",
#                   "x": "126.993052",
#                   "y": "37.534558",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 136,
#             "sectionTime": 2
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16191,
#           "totalWalk": 177,
#           "totalTime": 62,
#           "payment": 1700,
#           "busTransitCount": 3,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:22@1054:1:3:18@1808:1:14:21",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역.보광동입구",
#           "totalStationCount": 29,
#           "busStationCount": 29,
#           "subwayStationCount": 0,
#           "totalDistance": 16368,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 30
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 4965,
#             "sectionTime": 18,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "대치역6번출구.강남구민회관",
#             "endX": 127.064291,
#             "endY": 37.492776,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 107873,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000136",
#             "endArsID": "23-239",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 7648,
#             "sectionTime": 27,
#             "stationCount": 15,
#             "lane": [
#               {
#                 "busNo": "420",
#                 "type": 11,
#                 "busID": 1054,
#                 "busLocalBlID": "100100068",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "대치역6번출구.강남구민회관",
#             "startX": 127.064291,
#             "startY": 37.492776,
#             "endName": "한남대교전망카페",
#             "endX": 127.015815,
#             "endY": 37.524424,
#             "startID": 107873,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000136",
#             "startArsID": "23-239",
#             "endID": 206223,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000408",
#             "endArsID": "23-531",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 107698,
#                   "stationName": "은마아파트입구사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000160",
#                   "arsID": "23-263",
#                   "x": "127.059987",
#                   "y": "37.498752",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 111822,
#                   "stationName": "도곡초등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000161",
#                   "arsID": "23-264",
#                   "x": "127.056653",
#                   "y": "37.497653",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 107453,
#                   "stationName": "한티역2번출구.서울강남고용노동지청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000162",
#                   "arsID": "23-265",
#                   "x": "127.053893",
#                   "y": "37.496784",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107345,
#                   "stationName": "한티역7번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000206",
#                   "arsID": "23-310",
#                   "x": "127.051494",
#                   "y": "37.496044",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107185,
#                   "stationName": "역삼중학교.강남세브란스병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000207",
#                   "arsID": "23-311",
#                   "x": "127.047621",
#                   "y": "37.494652",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 106871,
#                   "stationName": "도곡1차아이파크.역삼청소년수련관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000208",
#                   "arsID": "23-312",
#                   "x": "127.041809",
#                   "y": "37.492848",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 106703,
#                   "stationName": "역삼럭키아파트.역삼월드메르디앙아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000187",
#                   "arsID": "23-291",
#                   "x": "127.038677",
#                   "y": "37.491886",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 106435,
#                   "stationName": "뱅뱅사거리.역삼동",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000190",
#                   "arsID": "23-294",
#                   "x": "127.033721",
#                   "y": "37.490349",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 3578,
#             "sectionTime": 15,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "421",
#                 "type": 11,
#                 "busID": 1808,
#                 "busLocalBlID": "100100409",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 10,
#             "startName": "한남대교전망카페",
#             "startX": 127.015815,
#             "startY": 37.524424,
#             "endName": "이태원역.보광동입구",
#             "endX": 126.994251,
#             "endY": 37.533803,
#             "startID": 206223,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000408",
#             "startArsID": "23-531",
#             "endID": 105094,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000190",
#             "endArsID": "03-284",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 151879,
#                   "stationName": "순천향병원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000225",
#                   "arsID": "03-319",
#                   "x": "127.0067",
#                   "y": "37.532691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 151878,
#                   "stationName": "한남역.용산노인종합복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000191",
#                   "arsID": "03-285",
#                   "x": "127.00664",
#                   "y": "37.53124",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 193883,
#                   "stationName": "한남동하이페리온",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000230",
#                   "arsID": "03-324",
#                   "x": "127.005508",
#                   "y": "37.527915",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 166679,
#                   "stationName": "보광동신동아아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000183",
#                   "arsID": "03-277",
#                   "x": "127.001498",
#                   "y": "37.525691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 166680,
#                   "stationName": "기업은행보광동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000185",
#                   "arsID": "03-279",
#                   "x": "126.999386",
#                   "y": "37.527953",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 166682,
#                   "stationName": "한국폴리텍1대학",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000188",
#                   "arsID": "03-282",
#                   "x": "126.9965",
#                   "y": "37.530569",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 105094,
#                   "stationName": "이태원역.보광동입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000190",
#                   "arsID": "03-284",
#                   "x": "126.994251",
#                   "y": "37.533803",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 88,
#             "sectionTime": 1
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16017,
#           "totalWalk": 497,
#           "totalTime": 66,
#           "payment": 1700,
#           "busTransitCount": 3,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:22@1050:1:26:41@789:1:34:38",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역1번출구.해밀턴호텔",
#           "totalStationCount": 26,
#           "busStationCount": 26,
#           "subwayStationCount": 0,
#           "totalDistance": 16514,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 28
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 4965,
#             "sectionTime": 18,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "대치역6번출구.강남구민회관",
#             "endX": 127.064291,
#             "endY": 37.492776,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 107873,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000136",
#             "endArsID": "23-239",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 272,
#             "sectionTime": 4
#           },
#           {
#             "trafficType": 2,
#             "distance": 8970,
#             "sectionTime": 30,
#             "stationCount": 15,
#             "lane": [
#               {
#                 "busNo": "402",
#                 "type": 11,
#                 "busID": 1050,
#                 "busLocalBlID": "100100063",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "대치역1번출구",
#             "startX": 127.061607,
#             "startY": 37.493971,
#             "endName": "순천향대학병원",
#             "endX": 127.00578,
#             "endY": 37.536396,
#             "startID": 107769,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000123",
#             "startArsID": "23-226",
#             "endID": 105318,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000068",
#             "endArsID": "03-162",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 107769,
#                   "stationName": "대치역1번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000123",
#                   "arsID": "23-226",
#                   "x": "127.061607",
#                   "y": "37.493971",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 107676,
#                   "stationName": "래미안.대치.팰리스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000124",
#                   "arsID": "23-227",
#                   "x": "127.058436",
#                   "y": "37.492513",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 107569,
#                   "stationName": "도곡역2번출구.동부센트레빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000116",
#                   "arsID": "23-219",
#                   "x": "127.056716",
#                   "y": "37.491724",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 107363,
#                   "stationName": "숙명여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000225",
#                   "arsID": "23-329",
#                   "x": "127.052511",
#                   "y": "37.489826",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 107230,
#                   "stationName": "매봉삼성아파트SK리더스뷰",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000212",
#                   "arsID": "23-316",
#                   "x": "127.048868",
#                   "y": "37.488192",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 193747,
#                   "stationName": "매봉역양재최의원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000213",
#                   "arsID": "23-317",
#                   "x": "127.044482",
#                   "y": "37.486247",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 106616,
#                   "stationName": "양재역말죽거리.강남베드로병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000214",
#                   "arsID": "23-318",
#                   "x": "127.037891",
#                   "y": "37.485256",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 106410,
#                   "stationName": "뱅뱅사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000006",
#                   "arsID": "22-006",
#                   "x": "127.032977",
#                   "y": "37.486703",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 2082,
#             "sectionTime": 11,
#             "stationCount": 4,
#             "lane": [
#               {
#                 "busNo": "110A",
#                 "type": 11,
#                 "busID": 789,
#                 "busLocalBlID": "100100016",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 8,
#             "startName": "순천향대학병원",
#             "startX": 127.00578,
#             "startY": 37.536396,
#             "endName": "이태원역1번출구.해밀턴호텔",
#             "endX": 126.993052,
#             "endY": 37.534558,
#             "startID": 105318,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000068",
#             "startArsID": "03-162",
#             "endID": 105070,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000096",
#             "endArsID": "03-190",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105070,
#                   "stationName": "이태원역1번출구.해밀턴호텔",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000096",
#                   "arsID": "03-190",
#                   "x": "126.993052",
#                   "y": "37.534558",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 136,
#             "sectionTime": 2
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 16323,
#           "totalWalk": 195,
#           "totalTime": 63,
#           "payment": 1700,
#           "busTransitCount": 3,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:22@1054:1:3:18@500:1:14:20",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역.보광동 입구",
#           "totalStationCount": 28,
#           "busStationCount": 28,
#           "subwayStationCount": 0,
#           "totalDistance": 16518,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 32
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 4965,
#             "sectionTime": 18,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "대치역6번출구.강남구민회관",
#             "endX": 127.064291,
#             "endY": 37.492776,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 107873,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000136",
#             "endArsID": "23-239",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 7648,
#             "sectionTime": 27,
#             "stationCount": 15,
#             "lane": [
#               {
#                 "busNo": "420",
#                 "type": 11,
#                 "busID": 1054,
#                 "busLocalBlID": "100100068",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "대치역6번출구.강남구민회관",
#             "startX": 127.064291,
#             "startY": 37.492776,
#             "endName": "한남대교전망카페",
#             "endX": 127.015815,
#             "endY": 37.524424,
#             "startID": 107873,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000136",
#             "startArsID": "23-239",
#             "endID": 206223,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000408",
#             "endArsID": "23-531",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 107823,
#                   "stationName": "은마아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000130",
#                   "arsID": "23-233",
#                   "x": "127.062854",
#                   "y": "37.495594",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 107698,
#                   "stationName": "은마아파트입구사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000160",
#                   "arsID": "23-263",
#                   "x": "127.059987",
#                   "y": "37.498752",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 111822,
#                   "stationName": "도곡초등학교",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000161",
#                   "arsID": "23-264",
#                   "x": "127.056653",
#                   "y": "37.497653",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 107453,
#                   "stationName": "한티역2번출구.서울강남고용노동지청",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000162",
#                   "arsID": "23-265",
#                   "x": "127.053893",
#                   "y": "37.496784",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107345,
#                   "stationName": "한티역7번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000206",
#                   "arsID": "23-310",
#                   "x": "127.051494",
#                   "y": "37.496044",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107185,
#                   "stationName": "역삼중학교.강남세브란스병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000207",
#                   "arsID": "23-311",
#                   "x": "127.047621",
#                   "y": "37.494652",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 106871,
#                   "stationName": "도곡1차아이파크.역삼청소년수련관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000208",
#                   "arsID": "23-312",
#                   "x": "127.041809",
#                   "y": "37.492848",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 106703,
#                   "stationName": "역삼럭키아파트.역삼월드메르디앙아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000187",
#                   "arsID": "23-291",
#                   "x": "127.038677",
#                   "y": "37.491886",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 106435,
#                   "stationName": "뱅뱅사거리.역삼동",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000190",
#                   "arsID": "23-294",
#                   "x": "127.033721",
#                   "y": "37.490349",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 15,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 0,
#             "sectionTime": 0
#           },
#           {
#             "trafficType": 2,
#             "distance": 3710,
#             "sectionTime": 15,
#             "stationCount": 6,
#             "lane": [
#               {
#                 "busNo": "400",
#                 "type": 11,
#                 "busID": 500,
#                 "busLocalBlID": "100100596",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 12,
#             "startName": "한남대교전망카페",
#             "startX": 127.015815,
#             "startY": 37.524424,
#             "endName": "이태원역.보광동 입구",
#             "endX": 126.994094,
#             "endY": 37.533675,
#             "startID": 206223,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000408",
#             "startArsID": "23-531",
#             "endID": 166805,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000189",
#             "endArsID": "03-283",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 105318,
#                   "stationName": "순천향대학병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000068",
#                   "arsID": "03-162",
#                   "x": "127.00578",
#                   "y": "37.536396",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 105225,
#                   "stationName": "한강진역.블루스퀘어",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000102",
#                   "arsID": "03-196",
#                   "x": "127.001657",
#                   "y": "37.540939",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 105193,
#                   "stationName": "한남동새마을금고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000100",
#                   "arsID": "03-194",
#                   "x": "127.000453",
#                   "y": "37.537018",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 105152,
#                   "stationName": "이태원119안전센터",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000098",
#                   "arsID": "03-192",
#                   "x": "126.996625",
#                   "y": "37.534796",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 166805,
#                   "stationName": "이태원역.보광동 입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000189",
#                   "arsID": "03-283",
#                   "x": "126.994094",
#                   "y": "37.533675",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 106,
#             "sectionTime": 2
#           }
#         ]
#       },
#       {
#         "pathType": 2,
#         "info": {
#           "trafficDistance": 15709,
#           "totalWalk": 592,
#           "totalTime": 67,
#           "payment": 1700,
#           "busTransitCount": 3,
#           "subwayTransitCount": 0,
#           "mapObj": "507:1:15:22@1050:1:26:40@1808:1:15:21",
#           "firstStartStation": "수서역현대벤쳐빌",
#           "lastEndStation": "이태원역.보광동입구",
#           "totalStationCount": 27,
#           "busStationCount": 27,
#           "subwayStationCount": 0,
#           "totalDistance": 16301,
#           "totalWalkTime": -1,
#           "checkIntervalTime": 100,
#           "checkIntervalTimeOverYn": "N",
#           "totalIntervalTime": 30
#         },
#         "subPath": [
#           {
#             "trafficType": 3,
#             "distance": 89,
#             "sectionTime": 1
#           },
#           {
#             "trafficType": 2,
#             "distance": 4965,
#             "sectionTime": 18,
#             "stationCount": 7,
#             "lane": [
#               {
#                 "busNo": "3011",
#                 "type": 12,
#                 "busID": 507,
#                 "busLocalBlID": "100100438",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 11,
#             "startName": "수서역현대벤쳐빌",
#             "startX": 127.102066,
#             "startY": 37.487671,
#             "endName": "대치역6번출구.강남구민회관",
#             "endX": 127.064291,
#             "endY": 37.492776,
#             "startID": 108996,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000294",
#             "startArsID": "23-401",
#             "endID": 107873,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "122000136",
#             "endArsID": "23-239",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 108996,
#                   "stationName": "수서역현대벤쳐빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000294",
#                   "arsID": "23-401",
#                   "x": "127.102066",
#                   "y": "37.487671",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 108949,
#                   "stationName": "수서역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000295",
#                   "arsID": "23-402",
#                   "x": "127.100507",
#                   "y": "37.48847",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 108653,
#                   "stationName": "일원주유소.삼성서울병원후문",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000287",
#                   "arsID": "23-994",
#                   "x": "127.087623",
#                   "y": "37.490705",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 108536,
#                   "stationName": "삼성서울병원사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000288",
#                   "arsID": "23-392",
#                   "x": "127.082632",
#                   "y": "37.489198",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 108079,
#                   "stationName": "주공4단지",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000246",
#                   "arsID": "23-350",
#                   "x": "127.069129",
#                   "y": "37.48383",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 107994,
#                   "stationName": "개포주공5단지경기여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000249",
#                   "arsID": "23-353",
#                   "x": "127.067442",
#                   "y": "37.486754",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 107939,
#                   "stationName": "개포동역.개포시장",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000250",
#                   "arsID": "23-354",
#                   "x": "127.06648",
#                   "y": "37.488639",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 107873,
#                   "stationName": "대치역6번출구.강남구민회관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000136",
#                   "arsID": "23-239",
#                   "x": "127.064291",
#                   "y": "37.492776",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 272,
#             "sectionTime": 4
#           },
#           {
#             "trafficType": 2,
#             "distance": 8529,
#             "sectionTime": 29,
#             "stationCount": 14,
#             "lane": [
#               {
#                 "busNo": "402",
#                 "type": 11,
#                 "busID": 1050,
#                 "busLocalBlID": "100100063",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 9,
#             "startName": "대치역1번출구",
#             "startX": 127.061607,
#             "startY": 37.493971,
#             "endName": "한남5거리",
#             "endX": 127.008281,
#             "endY": 37.532957,
#             "startID": 107769,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "122000123",
#             "startArsID": "23-226",
#             "endID": 105378,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000072",
#             "endArsID": "03-166",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 107769,
#                   "stationName": "대치역1번출구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000123",
#                   "arsID": "23-226",
#                   "x": "127.061607",
#                   "y": "37.493971",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 107676,
#                   "stationName": "래미안.대치.팰리스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000124",
#                   "arsID": "23-227",
#                   "x": "127.058436",
#                   "y": "37.492513",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 107569,
#                   "stationName": "도곡역2번출구.동부센트레빌",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000116",
#                   "arsID": "23-219",
#                   "x": "127.056716",
#                   "y": "37.491724",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 107363,
#                   "stationName": "숙명여고",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000225",
#                   "arsID": "23-329",
#                   "x": "127.052511",
#                   "y": "37.489826",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 107230,
#                   "stationName": "매봉삼성아파트SK리더스뷰",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000212",
#                   "arsID": "23-316",
#                   "x": "127.048868",
#                   "y": "37.488192",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 193747,
#                   "stationName": "매봉역양재최의원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000213",
#                   "arsID": "23-317",
#                   "x": "127.044482",
#                   "y": "37.486247",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 106616,
#                   "stationName": "양재역말죽거리.강남베드로병원",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000214",
#                   "arsID": "23-318",
#                   "x": "127.037891",
#                   "y": "37.485256",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 7,
#                   "stationID": 106410,
#                   "stationName": "뱅뱅사거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000006",
#                   "arsID": "22-006",
#                   "x": "127.032977",
#                   "y": "37.486703",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 8,
#                   "stationID": 106330,
#                   "stationName": "래미안아파트.파이낸셜뉴스",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000008",
#                   "arsID": "22-008",
#                   "x": "127.030872",
#                   "y": "37.491227",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 9,
#                   "stationID": 106188,
#                   "stationName": "신분당선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000010",
#                   "arsID": "22-010",
#                   "x": "127.029129",
#                   "y": "37.494853",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 10,
#                   "stationID": 106041,
#                   "stationName": "지하철2호선강남역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000012",
#                   "arsID": "22-012",
#                   "x": "127.026246",
#                   "y": "37.500867",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 11,
#                   "stationID": 105923,
#                   "stationName": "논현역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000014",
#                   "arsID": "22-014",
#                   "x": "127.023721",
#                   "y": "37.506306",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 12,
#                   "stationID": 105884,
#                   "stationName": "신사역",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "121000016",
#                   "arsID": "22-016",
#                   "x": "127.020661",
#                   "y": "37.512831",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 13,
#                   "stationID": 206223,
#                   "stationName": "한남대교전망카페",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "122000408",
#                   "arsID": "23-531",
#                   "x": "127.015815",
#                   "y": "37.524424",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 14,
#                   "stationID": 105378,
#                   "stationName": "한남5거리",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000072",
#                   "arsID": "03-166",
#                   "x": "127.008281",
#                   "y": "37.532957",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 143,
#             "sectionTime": 2
#           },
#           {
#             "trafficType": 2,
#             "distance": 2215,
#             "sectionTime": 12,
#             "stationCount": 6,
#             "lane": [
#               {
#                 "busNo": "421",
#                 "type": 11,
#                 "busID": 1808,
#                 "busLocalBlID": "100100409",
#                 "busCityCode": 1000,
#                 "busProviderCode": 4
#               }
#             ],
#             "intervalTime": 10,
#             "startName": "순천향병원입구",
#             "startX": 127.0067,
#             "startY": 37.532691,
#             "endName": "이태원역.보광동입구",
#             "endX": 126.994251,
#             "endY": 37.533803,
#             "startID": 151879,
#             "startStationCityCode": 1000,
#             "startStationProviderCode": 4,
#             "startLocalStationID": "102000225",
#             "startArsID": "03-319",
#             "endID": 105094,
#             "endStationCityCode": 1000,
#             "endStationProviderCode": 4,
#             "endLocalStationID": "102000190",
#             "endArsID": "03-284",
#             "passStopList": {
#               "stations": [
#                 {
#                   "index": 0,
#                   "stationID": 151879,
#                   "stationName": "순천향병원입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000225",
#                   "arsID": "03-319",
#                   "x": "127.0067",
#                   "y": "37.532691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 1,
#                   "stationID": 151878,
#                   "stationName": "한남역.용산노인종합복지관",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000191",
#                   "arsID": "03-285",
#                   "x": "127.00664",
#                   "y": "37.53124",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 2,
#                   "stationID": 193883,
#                   "stationName": "한남동하이페리온",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000230",
#                   "arsID": "03-324",
#                   "x": "127.005508",
#                   "y": "37.527915",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 3,
#                   "stationID": 166679,
#                   "stationName": "보광동신동아아파트",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000183",
#                   "arsID": "03-277",
#                   "x": "127.001498",
#                   "y": "37.525691",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 4,
#                   "stationID": 166680,
#                   "stationName": "기업은행보광동지점",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000185",
#                   "arsID": "03-279",
#                   "x": "126.999386",
#                   "y": "37.527953",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 5,
#                   "stationID": 166682,
#                   "stationName": "한국폴리텍1대학",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000188",
#                   "arsID": "03-282",
#                   "x": "126.9965",
#                   "y": "37.530569",
#                   "isNonStop": "N"
#                 },
#                 {
#                   "index": 6,
#                   "stationID": 105094,
#                   "stationName": "이태원역.보광동입구",
#                   "stationCityCode": 1000,
#                   "stationProviderCode": 4,
#                   "localStationID": "102000190",
#                   "arsID": "03-284",
#                   "x": "126.994251",
#                   "y": "37.533803",
#                   "isNonStop": "N"
#                 }
#               ]
#             }
#           },
#           {
#             "trafficType": 3,
#             "distance": 88,
#             "sectionTime": 1
#           }
#         ]
#       }
#     ]
#   }
# }