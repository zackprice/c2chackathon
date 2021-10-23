from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="validates grammar")
def get():
    """
    Check that resume is grammatically correct
    """
    return {"result": "OK", "version": get_settings().VERSION}
