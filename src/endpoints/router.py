from fastapi import APIRouter

from endpoints import sample
from endpoints import training
from endpoints import grammar
from endpoints import spellcheck
from endpoints import professionalism
from endpoints import textcount
from endpoints import resumescore
from endpoints import personalinfo

def api_router() -> APIRouter:
    router = APIRouter()
    router.include_router(
        sample.router, prefix="/sample", tags=["sample"]
    )
    router.include_router(
        training.router, prefix="/training", tags=["training"]
    )
    router.include_router(
        grammar.router, prefix="/grammar", tags=["grammar"]
    )
    router.include_router(
        spellcheck.router, prefix="/spellcheck", tags=["spellcheck"]
    )
    router.include_router(
        professionalism.router, prefix="/professionalism", tags=["professionalism"]
    )
    router.include_router(
        textcount.router, prefix="/textcount", tags=["textcount"]
    )
    router.include_router(
        resumescore.router, prefix="/resumescore", tags=["resumescore"]
    )
    router.include_router(
        personalinfo.router, prefix="/personalinfo", tags=["personalinfo"]
    )
    return router
