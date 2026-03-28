"""CLI tool to run raw SQL migrations from migrations/sql/ folder.

Usage:
    migrate-sql          (after pip install -e .)
    python -m app.migrate
"""

import logging
import pathlib
import sys

import sqlalchemy

from app.config import settings
from app.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

SQL_DIR = pathlib.Path(__file__).resolve().parent.parent / "migrations" / "sql"


def run() -> None:
    if not SQL_DIR.exists():
        logger.error("SQL migrations directory not found: %s", SQL_DIR)
        sys.exit(1)

    sql_files = sorted(SQL_DIR.glob("*.sql"))
    if not sql_files:
        logger.info("No .sql files found in %s", SQL_DIR)
        return

    engine = sqlalchemy.create_engine(settings.database_url_sync)

    with engine.begin() as conn:
        for path in sql_files:
            logger.info("Applying %s ...", path.name)
            sql = path.read_text(encoding="utf-8")
            conn.execute(sqlalchemy.text(sql))
            logger.info("Done: %s", path.name)

    engine.dispose()
    logger.info("All SQL migrations applied successfully")


if __name__ == "__main__":
    run()
