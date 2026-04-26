from fastapi import APIRouter, Query

from app.collections.schemas.api_schemas import CollectionsResponseSchema
from app.collections.use_cases.get_collections_use_case import get_collections_use_case

router = APIRouter(prefix="/collections")

@router.get("/")
async def get_collections(
    limit: int = Query(10),
    offset: int = Query(0),
) -> CollectionsResponseSchema:
    return await get_collections_use_case(limit, offset)
