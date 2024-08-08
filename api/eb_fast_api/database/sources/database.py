from pathlib import Path
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


Base = declarative_base()


def createEngine(
    filePath: str = str(Path(__file__).parent.absolute()),
    fileName: str = "earlybuddy.db",
) -> Engine:
    filePath += f"/{fileName}"
    DB_URL = "sqlite:///" + filePath
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
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