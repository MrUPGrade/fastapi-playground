from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from api import models
from sqlalchemy.orm import Session, subqueryload
from api.db import get_db

router = APIRouter()


class PostsViewModel(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True


@router.get("/", response_model=List[PostsViewModel])
def list_posts(user_id: int = None, db: Session = Depends(get_db)):
    posts_query = db.query(models.Post)
    if user_id is not None:
        posts_query = posts_query.filter(models.Post.user_id == user_id)
    return posts_query.all()


class PostAddViewModel(BaseModel):
    title: str
    content: str
    user_id: int


@router.post("/", response_model=PostsViewModel)
def add_post(post: PostAddViewModel, db: Session = Depends(get_db)):
    user = db.query(models.User).get(post.user_id)
    if not user:
        raise HTTPException(400)

    post = models.Post(title=post.title, content=post.content, user_id=user.id)
    db.add(post)
    db.commit()

    return post
