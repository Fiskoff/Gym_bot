from datetime import date

from sqlalchemy import ForeignKey, Date, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import BaseModel


class WorkoutsM(BaseModel):
    __tablename__ = "workouts"

    workout_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    workout_date: Mapped[date] = mapped_column(Date, nullable=False)
    name_workout: Mapped[str] = mapped_column(String, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
