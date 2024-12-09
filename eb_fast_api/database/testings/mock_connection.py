from eb_fast_api.database.sources.connection import createSessionMaker, createEngine


createdMockEngine = createEngine(host="0.0.0.0")


mockSessionMaker = createSessionMaker(engine=createdMockEngine)
