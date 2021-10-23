from fastapi import APIRouter, UploadFile, File
from config import get_settings
import requests
import json

router = APIRouter()


@router.get("/", summary="Grammar and Spelling check from languagetool.org")
def get(inputtext: str=""):
    """
    Returns grammar and spelling mistakes
    """
    r = requests.post('https://api.languagetoolplus.com/v2/check', data={'text': 'thas my number name theer','language': 'en-US'})
    objr = json.loads(r.text)
    returnmatches = []
    for match in objr['matches']:
        message = match['message']
        text = match['context']['text']
        error = f"{message} at {text}"
        returnmatches.append(error)
    if not returnmatches:
        
    return {"result": "OK", "version": get_settings().VERSION}

