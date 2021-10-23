from fastapi import APIRouter, UploadFile, File

from config import get_settings

router = APIRouter()


@router.get("/", summary="this is the summary")
def get():
    """
    This is the description
    """
    return {"result": "OK", "version": get_settings().VERSION}


@router.post("/")
async def post(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "type": file.content_type,
        "contents": await file.read()
    }