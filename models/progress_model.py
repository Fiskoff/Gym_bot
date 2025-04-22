from datetime import date

from sqlalchemy import ForeignKey, Date, Float
from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import BaseModel


class ProgressM(BaseModel):
    __tablename__ = "progress"

    progress_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    date: Mapped[date] = mapped_column(Date, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    body_fat_percentage: Mapped[float] = mapped_column(Float, nullable=True)
    muscle_mass: Mapped[float] = mapped_column(Float, nullable=True)