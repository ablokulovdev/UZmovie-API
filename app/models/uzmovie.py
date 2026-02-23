from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer,primary_key=True)
    title = Column(String(length=250),nullable=False)
    movie_img = Column(String,nullable=False)
    description = Column(Text)
    genre = Column(String,nullable=False)
    state = Column(String(length=250),nullable=False)
    active = Column(Boolean,default=True,nullable=False)
    year = Column(Integer,nullable=False)
    language = Column(String(length=100),nullable=False)
    duration = Column(Integer,nullable=False)
    age_limit = Column(Integer,nullable=False)
    treyler_url = Column(String,nullable=False)
    vedio_url = Column(String,nullable=False)
    
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"Movies (id={self.id}, name = {self.title} year = {self.year}, vedio_url = {self.vedio_url})"