from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session


class BaseRepository:
    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        async with async_session() as session:
            yield session
