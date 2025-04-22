from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from models.workout_model import WorkoutsM


class WorkoutDAL:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def create_workout(self, user_id:int, workout_date:date, name_workout:str, notes:str = None):
        self.session.add(WorkoutsM(user_id=user_id, workout_date=workout_date, name_workout=name_workout, notes=notes))
        await self.session.commit()