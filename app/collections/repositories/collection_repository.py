from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.collections.models.collection_model import Collection


class CollectionRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_collections(self, limit: int, offset: int) -> Sequence[Collection]:
        stmt = select(Collection).offset(offset).limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()
