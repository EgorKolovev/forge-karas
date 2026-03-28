# forge-karas

Backend course project.

## Stack

- **FastAPI** — web framework
- **PostgreSQL** — database
- **SQLAlchemy 2.0** — async ORM
- **Alembic** — schema migrations
- **Pydantic Settings** — configuration
- **Docker Compose** — runs everything

## Quick start

```bash
# 1. Copy env file and adjust if needed
cp .env.example .env

# 2. Build and start everything
docker compose up -d --build

# 3. App is running at http://localhost:8000
curl http://localhost:8000/health
```

## Entry point

`app/main.py` — creates the FastAPI application.

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
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── pyproject.toml
├── .env.example
└── README.md
```

## Database

Postgres runs in Docker alongside the app. Connection string is configured via `DATABASE_URL` in `.env`.

## Migrations

### Alembic (schema migrations)

```bash
# Create a new migration
docker compose exec app alembic revision --autogenerate -m "description"

# Apply all migrations
docker compose exec app alembic upgrade head
```

### Raw SQL migrations

Place `.sql` files in `migrations/sql/`. They are applied in alphabetical order.

```bash
docker compose exec app migrate-sql
```

## Logging

Configured in `app/logging_config.py`. Log level is set via `LOG_LEVEL` env var (default: `INFO`).
