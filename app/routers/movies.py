from fastapi import HTTPException, status
from random import randint
from typing import Annotated
from fastapi import APIRouter,Form, Query, UploadFile, File

from app.schemas.movies import MoviesListRespons
from app.db.database import LocalSession
from app.models.uzmovie import Movie


router = APIRouter(
    prefix="/movies",
    tags=["Movies Endpoint:"]
)


@router.get("",response_model=MoviesListRespons)
def movies_get(
    search: Annotated[str | None, Query(min_length=3, max_length=60)]=None,
    year: Annotated[int| None, Query(ge=0)]=None,
    page: Annotated[int, Query(ge=1)]=1,
    limit: Annotated[int, Query(ge=1, le=100)]=10
):
    
    db = LocalSession()

    
    if search is not None:
        movies = db.query(Movie).filter(Movie.title.ilike(f"%{search}%")).all()
        return MoviesListRespons(movies=movies)
    
    if year is not None:
         movies = db.query(Movie).filter(Movie.year == year).all()
         
         return MoviesListRespons(movies=movies)

    offset = (page-1)*limit
    
    movies = db.query(Movie).filter(Movie.active==True).offset(offset).limit(limit).all()
    count = db.query(Movie).filter(Movie.active==True).count()

    return MoviesListRespons(movies=movies)
    

    
@router.post("")
def create_movies(
    title: str = Form(),
    description : str | None = Form(None),
    movie_img: UploadFile = File(),
    genres: list[str] = Form(),
    state: str = Form(),
    year:int = Form(),
    language: str = Form("uz/rus"),
    duration: int = Form("500"),
    age_limit: int = Form(),
    treyler_url: str = Form("https//"),
    vedio_url: UploadFile = File()
):
    
    
    db = LocalSession()
    
    existing = db.query(Movie).filter(Movie.title == title).first()
    
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{title} Bunday kino mavjud.")

        
    vedio_path = str(f"movies/{randint(1,1000000000)}{vedio_url.filename}")
    img_path = str(f"movies/{randint(1,1000000000000)}{movie_img.filename}")
    
    with open(vedio_path,"wb") as f:
        contents = vedio_url.file.read()
        f.write(contents)
        
    with open(img_path,"wb") as f:
        contents = movie_img.file.read()
        f.write(contents)


    movies = Movie(
        title=title,
        movie_img=img_path,
        description=description,
        genre=genres,
        state=state,
        year=year,
        language=language,
        duration=duration,
        age_limit=age_limit,
        treyler_url=treyler_url,
        vedio_url=vedio_path
    )

    db.add(movies)
    db.commit()
    db.refresh(movies)

    return movies
