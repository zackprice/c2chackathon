from fastapi import APIRouter, UploadFile, File
from config import get_settings
import textstat

router = APIRouter()

MIN_READING_LEVEL = 8

@router.get("/", summary="Grade Reading Level")
def get(inputtext: str=""):
    """
    Return the estimated reading grade level of the input text as a float.
    Results are:
    4.9 or lower	average 4th-grade student or lower
    5.0–5.9	average 5th or 6th-grade student
    6.0–6.9	average 7th or 8th-grade student
    7.0–7.9	average 9th or 10th-grade student
    8.0–8.9	average 11th or 12th-grade student
    9.0–9.9	average 13th to 15th-grade (college) student
    """
    score = textstat.dale_chall_readability_score(text)
    ret = "Reading Level OK"
    if score < 8:
        ret = "Warning: Reading Level Low"

    return {"result": "OK", "version": get_settings().VERSION}

