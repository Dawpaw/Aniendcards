from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.router import router as post_router


from sqlalchemy import create_engine
from src.adapters.orm import metadata  # adjust import
from src.config import get_sqlite_uri

engine = create_engine(get_sqlite_uri())

app = FastAPI()

# FIXME remove
@app.on_event("startup")
def startup():
    metadata.create_all(engine)

origins = ["*"]  # TODO Change the actual origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
