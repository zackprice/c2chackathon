from fastapi import APIRouter, UploadFile, File

from config import get_settings

from comprehend_client import S3Client


router = APIRouter()


@router.get("/", summary="this is the summary")
def get():
    """
    This is the description
    """

    client = S3Client()

    response = client.get_object(bucket_name="c2chackathon", key="professionaltraining.cvs")
    return {"response": response}
    
