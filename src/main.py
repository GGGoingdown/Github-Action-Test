from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(settings)
    yield

app = FastAPI(
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": settings.api_key}




