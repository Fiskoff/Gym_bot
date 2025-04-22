from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserM


class UserDAL:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session


    async def create_user(self, user_id:int, username:str):
        self.session.add(UserM(user_id=user_id, username=username))
        await self.session.commit()


    async def get_user(self, user_id) -> UserM | None:
        result = await self.session.execute(select(UserM).where(UserM.user_id == user_id))
        return result.scalars().first()
