from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from eb_fast_api.env.sources.env import ENV_MYSQL


def createEngine(
    user: str = ENV_MYSQL.MYSQL_USER,
    pwd: str = ENV_MYSQL.MYSQL_PASSWORD,
    host: str = "eb_database",
    port: int = ENV_MYSQL.MYSQL_PORT,
    db: str = ENV_MYSQL.MYSQL_DATABASE,
) -> Engine:
    DB_URL = f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"
    engine = create_engine(
        DB_URL,
        pool_pre_ping=True,
        # echo=True,
    )
    return engine


engine = createEngine()


def checkConnection(engine: Engine = engine):
    try:
        engine.connect()
        print("Success Database Connect")
    except:
        raise "Fail Database Connect"


def createSessionMaker(engine: Engine = engine) -> sessionmaker[Session]:
    sessionMaker = sessionmaker(autoflush=False, bind=engine)
    return sessionMaker


sessionMaker = createSessionMaker()
