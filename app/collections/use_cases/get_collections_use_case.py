from app.collections.repositories.collection_repository import CollectionRepository
from app.collections.schemas.api_schemas import (
    CollectionsResponseSchema,
    CollectionSchema,
    MetadataSchema
)


async def get_collections_use_case(limit: int, offset: int) -> CollectionsResponseSchema:
    repository = CollectionRepository()
    collections = await repository.get_collections(limit, offset)
    items = [
        CollectionSchema.model_validate(collection, from_attributes=True)
        for collection in collections
    ]

    return CollectionsResponseSchema(
        metadata=MetadataSchema(
            total_count=len(items),
            limit=limit,
            offset=offset,
        ),
        collections=items,
    )
