from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.router_endcards import router as endcards_router
from src.entrypoints.router_auth import router as auth_router

from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from src.adapters import orm
from src.adapters.orm import metadata  # adjust import
from src.config import get_postgres_uri

engine = create_engine(get_postgres_uri())

@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)  
    yield

app = FastAPI(lifespan=lifespan)
orm.start_mappers()

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

app.include_router(endcards_router)
app.include_router(auth_router)
