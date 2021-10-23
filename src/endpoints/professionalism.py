from fastapi import APIRouter

from config import get_settings

from comprehend_client import ComprehendClient, ComprehendResponse, S3Client

router = APIRouter()


@router.get("/{text}", summary="validates grammar")
def get(text: str):
    """
    This is the description
    """
    client = ComprehendClient()
    response = client.classify_document(text=text, endponint_arn="arn:aws:comprehend:us-east-1:768862600548:document-classifier-endpoint/ProfesionalismChecker")

    return {"response": response}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}