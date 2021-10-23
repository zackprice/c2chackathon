from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="validates spellcheck")
def get():
    """
    Checks for any spelling issues
    """
    return {"result": "OK", "version": get_settings().VERSION}
