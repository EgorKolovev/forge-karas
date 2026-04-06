from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.collections.schemas import GetCollectionsResponseSchema
from app.collections.use_cases import get_collections_use_case
from app.database import get_session

router = APIRouter(prefix="/collections")

@router.get("/")
async def get_collections(
    session: AsyncSession = Depends(get_session)
) -> GetCollectionsResponseSchema:
    return await get_collections_use_case(session)
