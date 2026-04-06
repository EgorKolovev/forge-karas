from sqlalchemy.ext.asyncio import AsyncSession

from app.collections.repository import CollectionRepository
from app.collections.schemas import GetCollectionsResponseSchema, CollectionSchema, GetCollectionsResponseSchemaMetadata


async def get_collections_use_case(session: AsyncSession) -> GetCollectionsResponseSchema:
    repository = CollectionRepository(session)
    collections = await repository.get_collections()
    items = [
        CollectionSchema(
            id=collection.id,
            title=collection.title,
            description=collection.description,
            cover_image_url=collection.cover_image_url,
            target_url=collection.target_url,
            priority=collection.priority,
            start_date=collection.start_date.isoformat(),
        )
        for collection in collections
    ]
    return GetCollectionsResponseSchema(
        metadata=GetCollectionsResponseSchemaMetadata(
            total_count=67,
            limit=67,
            offset=67
        ),
        collections=items,
    )
