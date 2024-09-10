from eb_fast_api.database.sources.connection import createSessionMaker, createEngine
from unittest.mock import patch


def mockCommitInBaseCRUD():
    def mockCommit(self):
        print("This is mock commit")
        return

    patcher = patch(
        "eb_fast_api.database.sources.crud.base_crud.BaseCRUD.commit", new=mockCommit
    )
    patcher.start()


mockEngine = createEngine(host="0.0.0.0")


mockSessionMaker = createSessionMaker(engine=mockEngine)
