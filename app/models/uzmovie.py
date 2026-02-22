from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Boolean,
    DateTime
)
from sqlalchemy.orm import relationship
from app.db.database import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(length=250),nullable=False)
    description = Column(Text)
    genre = Column(String(length=50),nullable=False)
    state = Column(String(length=250),nullable=False)
    active = Column(Boolean,default=True,nullable=False)
    year = Column(Integer,nullable=False)
    language = Column(String(length=100),nullable=False)
    duration = Column(Integer,nullable=False)
    age_limit = Column(String(50),nullable=False)
    views_url = Column(String,nullable=False)
    treyler_url = Column(String,nullable=False)
    
    
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,onupdate=datetime.utcnow())
    
    
    