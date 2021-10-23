from fastapi import APIRouter, UploadFile, File
from config import get_settings

router = APIRouter()

MIN_PHRASE = 0
MAX_PHRASE = 100
MIN_SECTION = 0
MAX_SECTION = 100
MIN_CONTENTS = 0
MAX_CONTENTS = 100

@router.get("/", summary="Text length check")
def get(inputtext: str=""):
    """
    Validate the length of text in Phrases, Sections and the Entire Resume
    Returns a list of suggested changes.
    """
    
    return {"result": "OK", "version": get_settings().VERSION}

def checkphrase(inputtext):
    if inputtext:
        if inputtext < MIN_PHRASE:
            return f"Short Phrase Detected At: {inputtext[:20]}"
        if inputtext < MAX_PHRASE:
            return f"Long Phrase Detected At: {inputtext[:20]}"

def checksection(inputtext):
    if inputtext:
        if inputtext < MIN_SECTION:
            return f"Short Section Detected At: {inputtext[:20]}"
        if inputtext < MAX_SECTION:
            return f"Long Section Detected At: {inputtext[:20]}"


def checkcontents(inputtext):
    if inputtext:
        if inputtext < MIN_CONTENTS:
            return "Entire Contents Too Short"
        if inputtext < MAX_CONTENTS:
            return "Entire Contents Too Long"
