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


async def get_all_workouts(user_id: int) -> list:
    async with db_helper.session_factory() as session:
        workout_dal = WorkoutDAL(session)
        workouts = await workout_dal.get_workouts(user_id)
        result_list = []
        for workout in workouts:
            result_list.append(f"{workout['name_workout']}|{workout['workout_date']}")
        return result_list

async def get_id_workout_service(workout_name: str, workout_date: str) -> int:
    async with db_helper.session_factory() as session:
        workout_dal = WorkoutDAL(session)
        workout_id = await workout_dal.get_id_workout(workout_name, workout_date)
        return workout_id