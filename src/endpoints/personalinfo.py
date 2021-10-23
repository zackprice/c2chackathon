from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="gets personalinfo")
def get():
    """
    Checks to see if all personal information is present
    """
    return {"result": "OK", "version": get_settings().VERSION}
