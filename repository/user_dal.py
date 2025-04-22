from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserM


class UserDAL:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def create_user(self, user_id: int, username:str):
        new_user = UserM(user_id=user_id, username=username)
        self.session.add(new_user)
        await self.session.commit()