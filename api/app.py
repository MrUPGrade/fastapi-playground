from fastapi import FastAPI

from api import models
from api.db import engine
from api.resources import users, health, posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(posts.router, prefix="/posts")
app.include_router(health.router, prefix="/health")


@app.get("/")
def read_root():
    return {
        "msg": "Hello World!",
        "app": "FastAPI playgrond",
        "version": "0.1"
    }
