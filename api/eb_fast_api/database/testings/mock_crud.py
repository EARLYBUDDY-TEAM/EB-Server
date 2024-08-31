from pathlib import Path
from eb_fast_api.database.sources.crud import CRUD
from eb_fast_api.database.sources.database import createSessionMaker, createEngine


class MockCRUD(CRUD):
    def commit(self):
        return


mockEngine = createEngine(
    filePath=str(Path(__file__).parent.absolute()),
    fileName="mockdatabase.db",
)


mockSessionMaker = createSessionMaker(engine = mockEngine)