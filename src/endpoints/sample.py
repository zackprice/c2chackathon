from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/")
def sample():
    return {"result": "OK", "version": get_settings().VERSION}
