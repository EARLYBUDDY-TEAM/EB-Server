from eb_fast_api.database.sources.crud import CRUD
from eb_fast_api.database.sources.database import createSessionMaker, createEngine


class MockCRUD(CRUD):
    def commit(self):
        return


mockEngine = createEngine(host="0.0.0.0")


mockSessionMaker = createSessionMaker(engine=mockEngine)
