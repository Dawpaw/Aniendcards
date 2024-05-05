from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.posts.router import router as post_router

app = FastAPI()

origins = ["*"]  # TODO Change the actual origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
