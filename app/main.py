from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.db.database import initial_db
from app.routers.movies import router as movies_router



initial_db()

app = FastAPI(title="UZmovie API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # productionda aniq domain yoziladi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("movies", exist_ok=True)
app.mount("/movies", StaticFiles(directory="movies"), name="movies")


def insert_genre():
    from app.db.database import LocalSession
    from app.models.uzmovie import Genre
    db = LocalSession()
    genre01 = Genre(name="Fantastik")
    genre02 = Genre(name="Jangari")
    genre03 = Genre(name="Triller")
    genre04 = Genre(name="Komediya")

    db.add_all([genre01,genre02,genre03,genre04])
    db.commit()

app.include_router(movies_router)

