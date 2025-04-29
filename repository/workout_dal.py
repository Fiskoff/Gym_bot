from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from models.workout_model import WorkoutsM


class WorkoutDAL:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def create_workout(self, user_id:int, workout_date:str, name_workout:str, notes:str = None):
        self.session.add(WorkoutsM(user_id=user_id, workout_date=workout_date, name_workout=name_workout, notes=notes))
        await self.session.commit()

    async def get_last_workout(self, user_id: int) -> int:
        stmt = (
            select(WorkoutsM.workout_id)
            .where(WorkoutsM.user_id == user_id)
            .order_by(WorkoutsM.created_at.desc())
            .limit(1)
        )
        result = await self.session.execute(stmt)
        last_workout_id = result.scalar()
        return last_workout_id

    async def get_workouts(self, user_id: int) -> list[dict]:
        stmt = select(WorkoutsM).where(WorkoutsM.user_id == user_id)
        result = await self.session.execute(stmt)
        workouts = result.scalars().all()
        all_workouts = [workout.__dict__ for workout in workouts]
        return all_workouts

    async def get_id_workout(self, workout_name: str, workout_date: str) -> int:
        stmt = (
            select(WorkoutsM.workout_id)
            .where(and_(WorkoutsM.name_workout == workout_name, WorkoutsM.workout_date == workout_date))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        workout_id = result.scalars().all()
        return workout_id[0]