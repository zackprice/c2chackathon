from fastapi import APIRouter, UploadFile, File

from config import get_settings

from comprehend_client import S3Client


router = APIRouter()


@router.get("/", summary="returns the training data")
def get():
    """
    Retrieves the data used in the training of the classifiers
    """

    client = S3Client()

    response = client.get_object(bucket_name="c2chackathon", key="professionaltraining.cvs")
    return {"response": response}
    
