from datetime import datetime
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.config import settings

engine = create_async_engine(settings.database_url, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class BaseTimeModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column()
    updated_at: Mapped[datetime] = mapped_column()

class BaseIdModel(Base):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True)

async def get_session() -> AsyncSession:  # type: ignore[misc]
    async with async_session() as session:
        yield session
