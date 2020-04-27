from fastapi import FastAPI
from api.resources import users, health, posts
from api import models
from api.db import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(posts.router, prefix="/posts")
app.include_router(health.router, prefix="/health")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}
