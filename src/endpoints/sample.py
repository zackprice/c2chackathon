from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def sample():
    return {"result": "OK", "version": "1.0.0"}
