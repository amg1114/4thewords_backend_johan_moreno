
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.db.database import create_db_and_tables

from app.routers import auth_router, location_router, legend_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.mount("/images", StaticFiles(directory="uploads"), name="images")

app.include_router(auth_router)
app.include_router(location_router)
app.include_router(legend_router)