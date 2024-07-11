# from httpx import Response
# from eb_fast_api.domain.map.route.tests.mock_data import mockJsonDict
# from eb_fast_api.domain.map.route.sources import route_schema

# testJsonDict = {
#     'searchType' : 0,
#     'efeaf' : 1,
#     'paths' : [
#         {
#             'pathType' : 1,
#             'infos' : [
#                 {
#                     'totalTime' : 2,
#                     'payment' : 3,
#                     'busTransitCount' : 4,
#                     'subwayTransitCount' : 5
#                 }
#             ]
#         }
#     ]
# }

# testJsonDict = {
#     'searchType' : 0,
#     'efeaf' : 1,
#     'path' : []
# }

# def test_responseJson_to_schema():
#     mockResponse = Response(status_code=200, json=mockJsonDict)
#     mockResponseDict: dict = mockResponse.json()['result']
#     mockResponseDict
#     route = route_schema.Route.fromJson(mockResponseDict)


from eb_fast_api.domain.map.route.sources import route_schema

def test_simplifySubwayName():
    raws = ['수도권 3호선', '수도권 수인.분당선']
    results = ['3호선', '수인분당선']
    for i, name in enumerate(raws):
        result = route_schema.simplifySubwayName(name)
        if result != results[i]:
            raise Exception('Fail Test!')