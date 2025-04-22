from sqlalchemy.orm import Mapped, mapped_column
from models.base_model import BaseModel


class UserM(BaseModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)