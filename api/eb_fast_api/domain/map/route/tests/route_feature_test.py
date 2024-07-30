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