import logging

from fastapi import FastAPI

from app.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Forge Karas")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


logger.info("Application created")
