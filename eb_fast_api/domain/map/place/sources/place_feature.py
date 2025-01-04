from eb_fast_api.env.sources.env import ENV_API
from httpx import AsyncClient


async def getPlaceData(query: str, x: str, y: str):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    header = {"Authorization": f"KakaoAK {ENV_API.kakaomap}"}
    params = {
        "query": query,
        "x": x,
        "y": y,
        "sort": "accuracy",
    }

    async with AsyncClient() as client:
        response = await client.get(url=url, headers=header, params=params)
        return response


# {
#   "documents": [
#     {
#       "address_name": "서울 마포구 동교동 165-5",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1786432255",
#       "phone": "02-6010-0104",
#       "place_name": "카카오프렌즈 홍대플래그십스토어",
#       "place_url": "http://place.map.kakao.com/1786432255",
#       "road_address_name": "서울 마포구 양화로 162",
#       "x": "126.923919460392",
#       "y": "37.5563194254356"
#     },
#     {
#       "address_name": "서울 서초구 서초동 1305-7",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "653245473",
#       "phone": "02-6494-1100",
#       "place_name": "카카오프렌즈 강남플래그십스토어",
#       "place_url": "http://place.map.kakao.com/653245473",
#       "road_address_name": "서울 서초구 강남대로 429",
#       "x": "127.025811882515",
#       "y": "37.5008934694709"
#     },
#     {
#       "address_name": "부산 중구 광복동2가 44-1",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "43233680",
#       "phone": "051-256-0815",
#       "place_name": "카카오프렌즈 부산플래그십스토어",
#       "place_url": "http://place.map.kakao.com/43233680",
#       "road_address_name": "부산 중구 광복로 62",
#       "x": "129.03161963791288",
#       "y": "35.09906536614727"
#     },
#     {
#       "address_name": "전북특별자치도 전주시 완산구 전동 74",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1831095361",
#       "phone": "063-285-1230",
#       "place_name": "카카오프렌즈 전주한옥마을점",
#       "place_url": "http://place.map.kakao.com/1831095361",
#       "road_address_name": "전북특별자치도 전주시 완산구 팔달로 126",
#       "x": "127.148735902147",
#       "y": "35.8140143576911"
#     },
#     {
#       "address_name": "서울 강남구 삼성동 159-1",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "26338954",
#       "phone": "02-6002-1880",
#       "place_name": "카카오프렌즈 스타필드 코엑스몰점",
#       "place_url": "http://place.map.kakao.com/26338954",
#       "road_address_name": "",
#       "x": "127.06065824129524",
#       "y": "37.51023495145718"
#     },
#     {
#       "address_name": "경기 성남시 분당구 백현동 532",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "143299114",
#       "phone": "031-601-7225",
#       "place_name": "카카오프렌즈 판교아지트점",
#       "place_url": "http://place.map.kakao.com/143299114",
#       "road_address_name": "경기 성남시 분당구 판교역로 166",
#       "x": "127.1100869772751",
#       "y": "37.39581744474611"
#     },
#     {
#       "address_name": "서울 중구 남대문로2가 123",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1044004404",
#       "phone": "02-2118-5150",
#       "place_name": "카카오프렌즈 롯데영플라자본점",
#       "place_url": "http://place.map.kakao.com/1044004404",
#       "road_address_name": "서울 중구 남대문로 67",
#       "x": "126.9817250690476",
#       "y": "37.563474814632414"
#     },
#     {
#       "address_name": "서울 영등포구 영등포동4가 442",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1411970905",
#       "phone": "02-2638-2750",
#       "place_name": "카카오프렌즈 타임스퀘어점",
#       "place_url": "http://place.map.kakao.com/1411970905",
#       "road_address_name": "서울 영등포구 영중로 15",
#       "x": "126.90306008669398",
#       "y": "37.51710703022398"
#     },
#     {
#       "address_name": "서울 송파구 신천동 29",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "27375630",
#       "phone": "02-3213-4514",
#       "place_name": "카카오프렌즈 롯데월드몰 잠실점",
#       "place_url": "http://place.map.kakao.com/27375630",
#       "road_address_name": "서울 송파구 올림픽로 300",
#       "x": "127.10374045440543",
#       "y": "37.51387025493796"
#     },
#     {
#       "address_name": "서울 용산구 한강로3가 40-999",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "63582914",
#       "phone": "010-2897-6546",
#       "place_name": "카카오프렌즈 용산역 팝업스토어",
#       "place_url": "http://place.map.kakao.com/63582914",
#       "road_address_name": "서울 용산구 한강대로23길 55",
#       "x": "126.96457755024218",
#       "y": "37.529816802466584"
#     },
#     {
#       "address_name": "대구 동구 신천동 1506",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "2078031633",
#       "phone": "053-661-6942",
#       "place_name": "카카오프렌즈 신세계백화점 동대구점",
#       "place_url": "http://place.map.kakao.com/2078031633",
#       "road_address_name": "대구 동구 동부로 149",
#       "x": "128.62895124045",
#       "y": "35.8777808953246"
#     },
#     {
#       "address_name": "제주특별자치도 제주시 용담이동 2002",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "981854961",
#       "phone": "064-740-9731",
#       "place_name": "카카오프렌즈 제주공항JDC면세점",
#       "place_url": "http://place.map.kakao.com/981854961",
#       "road_address_name": "제주특별자치도 제주시 공항로 2",
#       "x": "126.49381921775688",
#       "y": "33.507112103989996"
#     },
#     {
#       "address_name": "서울 중구 봉래동2가 122-11",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1256445945",
#       "phone": "010-2743-6546",
#       "place_name": "카카오프렌즈 서울역점",
#       "place_url": "http://place.map.kakao.com/1256445945",
#       "road_address_name": "서울 중구 한강대로 405",
#       "x": "126.970586543568",
#       "y": "37.5546860417757"
#     },
#     {
#       "address_name": "서울 중구 충무로1가 52-5",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "1777071768",
#       "phone": "02-6370-4278",
#       "place_name": "카카오프렌즈 신세계면세 명동점",
#       "place_url": "http://place.map.kakao.com/1777071768",
#       "road_address_name": "서울 중구 소공로 63",
#       "x": "126.981089600579",
#       "y": "37.5609663400347"
#     },
#     {
#       "address_name": "제주특별자치도 제주시 연동 252-43",
#       "category_group_code": "",
#       "category_group_name": "",
#       "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
#       "distance": "",
#       "id": "151657875",
#       "phone": "",
#       "place_name": "카카오프렌즈 제주신라면세점",
#       "place_url": "http://place.map.kakao.com/151657875",
#       "road_address_name": "제주특별자치도 제주시 노연로 69",
#       "x": "126.48752655406",
#       "y": "33.4862757180351"
#     }
#   ],
#   "meta": {
#     "is_end": false,
#     "pageable_count": 45,
#     "same_name": {
#       "keyword": "카카오 프렌즈",
#       "region": [],
#       "selected_region": ""
#     },
#     "total_count": 62
#   }
# }
