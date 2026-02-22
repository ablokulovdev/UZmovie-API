from typing import List,Annotated
from fastapi import APIRouter,Form, Query

from app.schemas.movies import MoviesListRespons,MoviesResponses
from app.db.database import LocalSession
from app.models.uzmovie import Movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies Endpoint:"]
)



@router.get("",response_model=List[MoviesResponses])
def movies_get(
    search: Annotated[str | None, Query(min_length=3, max_length=60)]=None,
    year: Annotated[int| None, Query(ge=0)]=None,
    page: Annotated[int, Query(ge=1)]=1,
    limit: Annotated[int, Query(ge=1, le=100)]=10
):
    
    db = LocalSession()
    
    if search is not None:
        movies = db.query(Movie).filter(Movie.name.ilike(f"%{search}%")).all()
        return movies
    
    if year is not None:
         movies = db.query(Movie).filter(Movie.year == year).all()
         
         return movies

    offset = (page-1)*limit
    
    movies = db.query(Movie).offset(offset).limit(limit).all()
    
    return movies
    

    
@router.post("", response_model=MoviesResponses)
def create_movies(
    name: str = Form("Under The demo"),
    description : str | None = Form(None),
    genre: str = Form("Jangari"),
    state: str = Form("AQSH"),
    year:int = Form(),
    language: str = Form("uz/rus"),
    duration: str = Form("500"),
    age_limit: str = Form("18+"),
    views_url: str = Form("https//underthedemo"),
    treyler_url: str = Form("https//youtebe"),
):
    db = LocalSession()
    
    movies = Movie(
        name=name,
        description=description,
        genre=genre,
        state=state,
        year=year,
        language=language,
        duration=duration,
        age_limit=age_limit,
        views_url=views_url,
        treyler_url=treyler_url
    )
    
    db.add(movies)
    db.commit()
    db.refresh(movies)

    return movies

