from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.collections.models import Collection


class CollectionRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_collections(self) -> Sequence[Collection]:
        stmt = select(Collection)
        result = await self.session.scalars(stmt)
        return result.all()
