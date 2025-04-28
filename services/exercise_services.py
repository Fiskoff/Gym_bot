from repository.exercise_dal import ExerciseDAL
from core.db_helper import db_helper


async def create_new_exercise(workout_id: int, exercise_name: str, sets: int, reps: int, weight: int):
    async with db_helper.session_factory() as session:
        new_exercise = ExerciseDAL(session)
        await new_exercise.create_exercise(workout_id, exercise_name, sets, reps, weight)
