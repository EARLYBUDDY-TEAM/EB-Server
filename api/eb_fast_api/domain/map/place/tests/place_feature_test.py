import pytest, httpx
from eb_fast_api.domain.map.place.sources import place_feature


@pytest.mark.asyncio
async def test_getPlaceData(fakeGet):
    # given
    statusCode = 200
    json = {'test' : 'test'}
    fakeGet.return_value = httpx.Response(
        statusCode,
        json = json,
        request = httpx.Request('GET', 'testURL'),
    )

    # when
    result = await place_feature.getPlaceData('', '', '')

    # then
    assert result.status_code == statusCode
    assert result.json() == json