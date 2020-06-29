from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from api import models
from sqlalchemy.orm import Session, subqueryload
from api.db import get_db

router = APIRouter()


class UserListViewModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserDetailsViewModel(BaseModel):
    id: int
    name: str
    post_count: int


@router.get("/", response_model=List[UserListViewModel])
def list_users(db: Session = Depends(get_db)) -> List[UserListViewModel]:
    users = db.query(models.User).filter(models.User.is_active == True).all()
    return users


@router.get("/{user_id}", response_model=UserDetailsViewModel)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).options(
        subqueryload(models.User.posts)
    ).get(user_id)

    if not user:
        raise HTTPException(status_code=404)
    post_count = len(user.posts)

    return {
        "name": user.name,
        "id": user.id,
        "post_count": post_count
    }
