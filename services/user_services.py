from core.db_helper import db_helper
from repository.user_dal import UserDAL


async def create_new_user(user_id: int, username:str):
    async with db_helper.session_factory() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            await user_dal.create_user(user_id=user_id, username=username)
