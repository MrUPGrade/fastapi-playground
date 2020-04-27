from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/echo")
def echo():
    return {"message": "hi"}
