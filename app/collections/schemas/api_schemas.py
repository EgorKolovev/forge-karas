from datetime import datetime
from typing import List

from pydantic import BaseModel
from uuid import UUID

class MetadataSchema(BaseModel):
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
    start_date: datetime

class CollectionsResponseSchema(BaseModel):
    metadata: MetadataSchema
    collections: List[CollectionSchema]