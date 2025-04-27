from sqlalchemy import ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import BaseModel


class WorkoutsM(BaseModel):
    __tablename__ = "workouts"

    workout_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    workout_date: Mapped[str] = mapped_column(String, nullable=False)
    name_workout: Mapped[str] = mapped_column(String, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
