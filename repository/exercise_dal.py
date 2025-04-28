from sqlalchemy.ext.asyncio import AsyncSession

from models.exercise_model import ExerciseM


class ExerciseDAL:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def create_exercise(self, workout_id: int, exercise_name: str, sets: int, reps: int, weight: int):
        self.session.add(ExerciseM(
            workout_id=workout_id,
            exercise_name=exercise_name,
            sets=sets,
            reps=reps,
            weight=weight
        ))
        await self.session.commit()

