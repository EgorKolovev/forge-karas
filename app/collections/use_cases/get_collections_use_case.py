from app.collections.repositories.collection_repository import CollectionRepository
from app.collections.schemas.api_schemas import (
    CollectionsResponseSchema,
    MetadataSchema
)


async def get_collections_use_case(limit: int, offset: int) -> CollectionsResponseSchema:
    repository = CollectionRepository()
    collections = await repository.get_collections(limit, offset)

    return CollectionsResponseSchema(
        metadata=MetadataSchema(
            total_count=len(collections),
            limit=limit,
            offset=offset,
        ),
        collections=collections,
    )
