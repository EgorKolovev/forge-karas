import logging

from fastapi import FastAPI

from app.collections.router import router as collections_router
from app.logging_config import setup_logging

logger = logging.getLogger(__name__)


async def health() -> dict[str, str]:
    return {"status": "ok"}


def add_routers(app: FastAPI) -> None:
    app.include_router(collections_router)
    app.add_api_route("/health", health, methods=["GET"])


def init_app() -> FastAPI:
    setup_logging()

    app = FastAPI(title="Forge Karas")
    add_routers(app)

    logger.info("Application created")
    return app


app = init_app()
