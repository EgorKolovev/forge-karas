from typing import Sequence

from sqlalchemy import select

from app.collections.models.collection import Collection
from app.collections.schemas.api_schemas import CollectionSchema
from app.repositories import BaseRepository


class CollectionRepository(BaseRepository):
    async def get_collections(self, limit: int, offset: int) -> Sequence[CollectionSchema]:
        stmt = select(Collection).offset(offset).limit(limit)
        async with self.get_session() as session:
            result = await session.scalars(stmt)
            return [
                CollectionSchema.model_validate(collection, from_attributes=True)
                for collection in result.all()
            ]
