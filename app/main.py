from fastapi import FastAPI

from app.db.database import initial_db
from app.routers.movies import router as movies_router


initial_db()

app = FastAPI(title="UZmovie API")


app.include_router(movies_router)

