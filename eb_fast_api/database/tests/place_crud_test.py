from eb_fast_api.database.sources.model.models import Place


def test_place_create_and_read(mockPlaceCRUD):
    # given
    place = Place.mock()

    # when
    mockPlaceCRUD.create(place=place)

    # then
    fetched_place_dict = mockPlaceCRUD.read(place_id=place.id)
    expect_place_dict = place.to_dict()
    assert expect_place_dict == fetched_place_dict


def test_place_create_check_duplicate(mockPlaceCRUD):
    # given
    place1 = Place.mock()
    place2 = Place.mock()
    place3 = Place.mock()

    # when
    mockPlaceCRUD.create(place=place1)
    mockPlaceCRUD.create(place=place2)
    mockPlaceCRUD.create(place=place3)
    place2.refCount = 0
    place3.refCount = 0

    # then
    fetched_place_dict = mockPlaceCRUD.read(place_id=place1.id)
    assert place1.to_dict() == fetched_place_dict
    assert place2.to_dict() == fetched_place_dict
    assert place3.to_dict() == fetched_place_dict
