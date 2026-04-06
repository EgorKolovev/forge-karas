from typing import List

from pydantic import BaseModel, HttpUrl
from uuid import UUID

class GetCollectionsResponseSchemaMetadata(BaseModel):
    total_count: int
    limit: int
    offset: int

class CollectionSchema(BaseModel):
    id: UUID
    title: str
    description: str
    cover_image_url: str
    target_url: str
    priority: int
    start_date: str

class GetCollectionsResponseSchema(BaseModel):
    metadata: GetCollectionsResponseSchemaMetadata
    collections: List[CollectionSchema]