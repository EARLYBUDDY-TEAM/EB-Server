from eb_fast_api.database.sources.connection import createSessionMaker, createEngine


def def_create_mock_engine():
    return createEngine(host="0.0.0.0")


createdMockEngine = def_create_mock_engine()


mockSessionMaker = createSessionMaker(engine=createdMockEngine)
