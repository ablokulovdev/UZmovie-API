from datetime import datetime
from pydantic import BaseModel


class MoviesRespons(BaseModel):
    
    id : int
    title: str
    movie_img: str
    description: str | None = None
    genre: str
    state: str
    active: bool
    year: int
    language: str
    duration: int
    age_limit: int
    treyler_url: str
    vedio_url: str
    created_at: datetime
    updated_at : datetime | None = None  
    
    class Config:
        from_attributes = True
        
        
class MoviesListRespons(BaseModel):
    
    movies: list[MoviesRespons]
    count: int | None = None
    
    class Config:
        from_attributes = True
