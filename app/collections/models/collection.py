from datetime import datetime
from uuid import UUID
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY, UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import BaseIdModel, BaseTimeModel


class Collection(BaseIdModel, BaseTimeModel):
    __tablename__ = "collections"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Название подборки",
    )
    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Описание подборки",
    )
    cover_image_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Ссылка на изображение обложки подборки",
    )
    target_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Ссылка для перехода при выборе подборки",
    )
    priority: Mapped[int] = mapped_column(
        comment="Приоритет сортировки подборки",
    )
    start_date: Mapped[datetime] = mapped_column(
        comment="Дата начала действия подборки",
    )
    product_ids: Mapped[list[UUID]] = mapped_column(
        ARRAY(PGUUID(as_uuid=True)),
        nullable=False,
        comment="Идентификаторы продуктов, входящих в подборку",
    )
