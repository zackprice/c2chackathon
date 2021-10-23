from fastapi import APIRouter

from config import get_settings

router = APIRouter()


@router.get("/", summary="validates resumescore")
def get():
    """
    Produce an overall score of your resume
    """
    return {"result": "OK", "version": get_settings().VERSION}
