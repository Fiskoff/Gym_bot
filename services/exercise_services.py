from repository.exercise_dal import ExerciseDAL
from core.db_helper import db_helper


async def create_new_exercise(workout_id: int, exercise_name: str, sets: int, reps: int, weight: int):
    async with db_helper.session_factory() as session:
        new_exercise = ExerciseDAL(session)
        await new_exercise.create_exercise(workout_id, exercise_name, sets, reps, weight)


async def get_exercise_for_workout_service(workout_id: int) -> list[dict]:
    async with db_helper.session_factory() as session:
        new_exercise = ExerciseDAL(session)
        object_get_exercise_select = await new_exercise.get_exercise_for_workout(workout_id)
        list_exersice = []
        for exercise_dict in object_get_exercise_select:
            exersice_dict = {}
            for key, value in exercise_dict.items():
                if key == "_sa_instance_state":
                    continue
                exersice_dict[key] = value
            list_exersice.append(exersice_dict)
        return list_exersice
