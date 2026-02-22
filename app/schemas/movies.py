from pydantic import BaseModel
from typing import List
    

class MoviesResponses(BaseModel):
    
    id: int
    name : str
    description: str | None = None
    genre: str
    state : str
    active : bool
    language: str
    duration: int
    age_limit : str
    views_url : str
    treyler_url : str
    
    
    class Config:
        from_attributes = True
    
    
    
class MoviesListRespons (BaseModel):
    
    movies : List[MoviesResponses]
    count: int | None = None
    
    class Config:
        from_attributes = True