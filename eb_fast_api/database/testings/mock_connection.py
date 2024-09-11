from eb_fast_api.database.sources.connection import createSessionMaker, createEngine


mockEngine = createEngine(host="0.0.0.0")


mockSessionMaker = createSessionMaker(engine=mockEngine)
