from datetime import datetime
from uuid import UUID
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY, UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import BaseIdModel, BaseTimeModel


class Collection(BaseIdModel, BaseTimeModel):
    __tablename__ = "collections"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    cover_image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    target_url: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column()
    start_date: Mapped[datetime] = mapped_column()
    product_ids: Mapped[list[UUID]] = mapped_column(
        ARRAY(PGUUID(as_uuid=True)),
        nullable=False,
    )
