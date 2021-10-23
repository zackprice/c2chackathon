from fastapi import APIRouter

from endpoints import sample


def api_router() -> APIRouter:
    router = APIRouter()
    router.include_router(
        sample.router, prefix="/sample", tags=["sample"]
    )
    return router
