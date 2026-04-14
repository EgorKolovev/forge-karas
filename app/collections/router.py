from fastapi import APIRouter, Query
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.collections.schemas.api_schemas import CollectionsResponseSchema
from app.collections.use_cases.get_collections_use_case import get_collections_use_case
from app.database import get_session

router = APIRouter(prefix="/collections")

@router.get("/")
async def get_collections(
    limit: int = Query(10),
    offset: int = Query(0),
    session: AsyncSession = Depends(get_session)
) -> CollectionsResponseSchema:
    return await get_collections_use_case(limit, offset, session)
