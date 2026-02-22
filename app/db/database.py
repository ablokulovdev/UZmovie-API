from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import config


DB_URL = URL.create(
    
    drivername = "postgresql+psycopg2",
    database   = config.DB_NAME,
    username   = config.DB_USER,
    password   = config.DB_PASS,
    port       = config.DB_PORT,
    host       = config.DB_HOST
)

engine = create_engine(url=DB_URL)
LocalSession = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def initial_db():
    from app.models import uzmovie
    Base.metadata.create_all(engine)