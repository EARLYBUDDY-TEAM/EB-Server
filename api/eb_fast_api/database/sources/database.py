from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DB_URL = "sqlite:///./eb_fast_api/database/earlybuddy.db"
Base = declarative_base()
engine = create_engine(DB_URL, connect_args={"check_same_thread" : False})
SessionLocal = sessionmaker(autoflush=False, bind=engine)