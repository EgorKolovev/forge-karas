# forge-karas

Backend course project.

## Stack

- **FastAPI** — web framework
- **PostgreSQL** — database (runs in Docker)
- **SQLAlchemy 2.0** — async ORM
- **Alembic** — schema migrations
- **Pydantic Settings** — configuration

## Quick start

```bash
# 1. Start the database
docker compose up -d

# 2. Install dependencies
pip install -e .

# 3. Run Alembic migrations
alembic upgrade head

# 4. Run SQL migrations (from migrations/sql/)
migrate-sql

# 5. Start the app
uvicorn app.main:app --reload
```

## Entry point

`app/main.py` — creates the FastAPI application.

```
uvicorn app.main:app --reload
```

## Project structure

```
forge-karas/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── config.py          # Settings from .env
│   ├── database.py        # SQLAlchemy engine & session
│   ├── logging_config.py  # Logging setup
│   └── migrate.py         # CLI: apply SQL migrations
├── migrations/
│   ├── versions/          # Alembic auto-generated migrations
│   ├── sql/               # Raw .sql migration files
│   ├── env.py             # Alembic env
│   └── script.py.mako     # Alembic template
├── alembic.ini
├── docker-compose.yml
├── pyproject.toml
├── .env.example
└── README.md
```

## Database

Postgres runs in Docker:

```bash
docker compose up -d
```

Connection string is configured via `DATABASE_URL` in `.env`.

## Migrations

### Alembic (schema migrations)

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply all migrations
alembic upgrade head
```

### Raw SQL migrations

Place `.sql` files in `migrations/sql/`. They are applied in alphabetical order.

```bash
migrate-sql
```

## Logging

Configured in `app/logging_config.py`. Log level is set via `LOG_LEVEL` env var (default: `INFO`).
