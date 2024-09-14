from eb_fast_api.database.sources.model.models import Place


def test_placeCreate(mockPlaceCRUD):
    place = Place.mock()

    mockPlaceCRUD.create(place=place)

    fetchedPlace = mockPlaceCRUD.read(placeID=place.id)
    assert place == fetchedPlace


def test_placeRead(mockPlaceCRUD):
    place = Place.mock()

    mockPlaceCRUD.create(place=place)

    fetchedPlace = mockPlaceCRUD.read(placeID=place.id)
    assert place == fetchedPlace


def test_placeCreate_check_duplicate(mockPlaceCRUD):
    place1 = Place.mock()
    place2 = Place.mock()
    place3 = Place.mock()

    mockPlaceCRUD.create(place=place1)
    mockPlaceCRUD.create(place=place2)
    mockPlaceCRUD.create(place=place3)

    placeCount = mockPlaceCRUD.session.query(Place).count()
    assert placeCount == 1