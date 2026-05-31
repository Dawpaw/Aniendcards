from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.router import router as post_router

from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from src.adapters.orm import metadata  # adjust import
from src.config import get_postgres_uri

engine = create_engine(get_postgres_uri())

@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)  
    yield

app = FastAPI(lifespan=lifespan)

# TODO Update once I know production domain
origins = [
    "http://localhost:5173",   # local dev
    "http://localhost:3000",   # docker frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
