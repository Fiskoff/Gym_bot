from core.db_helper import db_helper
from repository.user_dal import UserDAL


async def create_new_user(user_id: int, username: str):
    async with db_helper.session_factory() as session:
        user_dal = UserDAL(session)
        user = await user_dal.get_user(user_id)
        if user is None:
            await user_dal.create_user(user_id, username)
            return "создан"
        return "существует"
