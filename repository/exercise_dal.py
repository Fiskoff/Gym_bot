from sqlalchemy import select
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

    async def get_exercise_for_workout(self, workout_id: int) -> dict:
        stmt = select(ExerciseM).where(ExerciseM.workout_id == workout_id)
        result = await self.session.execute(stmt)
        exercise_all = result.scalars().all()
        exercise_all_dict = [exercise.__dict__ for exercise in exercise_all]
        return exercise_all_dict

