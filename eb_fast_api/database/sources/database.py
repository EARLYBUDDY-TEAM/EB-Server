from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from eb_fast_api.env.sources.env import ENV_MYSQL


Base = declarative_base()


def createEngine(
    user: str = ENV_MYSQL.MYSQL_USER,
    pwd: str = ENV_MYSQL.MYSQL_PASSWORD,
    host: str = "eb_database",
    port: int = ENV_MYSQL.MYSQL_PORT,
    db: str = ENV_MYSQL.MYSQL_DATABASE,
) -> Engine:
    DB_URL = f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"
    engine = create_engine(DB_URL)
    return engine


engine = createEngine()


def createTable(engine: Engine = engine):
    Base.metadata.create_all(bind=engine)


def dropTable(engine: Engine = engine):
    Base.metadata.drop_all(bind=engine)


def createSessionMaker(engine: Engine = engine) -> sessionmaker[Session]:
    sessionMaker = sessionmaker(autoflush=False, bind=engine)
    return sessionMaker


sessionMaker = createSessionMaker()
