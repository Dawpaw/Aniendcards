from fastapi import FastAPI
from src.posts.router import router as post_router

app = FastAPI()

app.include_router(post_router)