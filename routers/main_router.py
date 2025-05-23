from aiogram import Router

from routers.exercise_fsm import exercise_fsm_router
from routers.user_router import user_router
from routers.workoun_router import workout_router


main_router = Router()

main_router.include_router(user_router)
main_router.include_router(workout_router)
main_router.include_router(exercise_fsm_router)