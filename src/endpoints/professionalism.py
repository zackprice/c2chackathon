from fastapi import APIRouter

from config import get_settings

from comprehend_client import ComprehendClient, ComprehendResponse, S3Client

router = APIRouter()


@router.get("/{text}", summary="validates professionalism")
def get(text: str):
    """
    Uses machine learning to classify the degree of Professionalism of your resume
    """
    client = ComprehendClient()
    response = client.classify_document(text=text, endponint_arn="arn:aws:comprehend:us-east-1:768862600548:document-classifier-endpoint/ProfesionalismChecker")
    classes = response.Classes
    for clazz in classes:
        if clazz.Name == "PROFESSIONAL" and clazz.Score >= 0.65:
            return{"result": f"Your Professionalism score is: {clazz.Score*100} ! This means that your resume is on the right track!"}
        else:
            return{"result": f"Your Professionalism score is:  {clazz.Score*100}! To improve your score check out our resources on our Resources tab!"}
