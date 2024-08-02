import pytest
from pathlib import Path
from eb_fast_api.database.sources.crud import CRUD
from eb_fast_api.database.sources.database import createSessionMaker


@pytest.fixture(scope="session")
def withMockCRUD():
    sessionMaker = createSessionMaker(
        filePath=str(Path(__file__).parent.absolute()),
        fileName="mockdatabase.db",
    )
    with CRUD(sessionMaker=sessionMaker) as crud:
        yield crud


@pytest.fixture(scope="function")
def mockCRUD(withMockCRUD):
    yield withMockCRUD
    withMockCRUD.rollback()
