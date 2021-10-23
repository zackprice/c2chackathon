from fastapi import APIRouter

from endpoints import sample, training


def api_router() -> APIRouter:
    router = APIRouter()
    router.include_router(
        sample.router, prefix="/sample", tags=["sample"]
    )
    router.include_router(
        training.router, prefix="/training", tags=["training"]
    )
    return router


