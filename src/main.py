from fastapi import FastAPI

from config import get_settings
from endpoints.router import api_router

app = FastAPI()

app.include_router(api_router(), prefix=get_settings().API_V1_STR)
