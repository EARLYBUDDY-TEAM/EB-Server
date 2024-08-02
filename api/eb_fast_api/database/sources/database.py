from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


Base = declarative_base()


def createSessionMaker(
    filePath: str = str(Path(__file__).parent.absolute()),
    fileName: str = "earlybuddy.db",
) -> sessionmaker[Session]:
    filePath += f"/{fileName}"
    DB_URL = "sqlite:///" + filePath
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    sessionMaker = sessionmaker(autoflush=False, bind=engine)
    return sessionMaker