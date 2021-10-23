from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="this is the summary")
def sample():
    """
    This is the description
    """
    return {"result": "OK", "version": get_settings().VERSION}
