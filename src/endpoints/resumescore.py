from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="validates resumescore")
def get():
    """
    This is the description
    """
    return {"result": "OK", "version": get_settings().VERSION}
