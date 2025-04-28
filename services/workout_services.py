from core.db_helper import db_helper
from repository.workout_dal import WorkoutDAL


async def create_new_workout(user_id:int, workout_date:str, name_workout:str, notes:str = None):
    async with db_helper.session_factory() as session:
        workout_dal = WorkoutDAL(session)
        await workout_dal.create_workout(user_id, workout_date, name_workout, notes)


async def get_last_workout_service(user_id: int) -> int:
    async with db_helper.session_factory() as session:
        last_workout = WorkoutDAL(session)
        return await last_workout.get_last_workout(user_id)