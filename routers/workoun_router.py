from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from routers.keyboard import workout_button, workouts_buttons
from routers.workout_fsw_router import workout_fsm_router


workout_router = Router()
workout_router.include_router(workout_fsm_router)


@workout_router.message(F.text == "Тренировка")
async def callback_workouts(message: Message):
    await message.answer(text="Раздел с тренировками", reply_markup=workout_button)


@workout_router.callback_query(F.data == "workouts")
async def callback_workouts(callback: CallbackQuery):
    await callback.answer("Выбрали тренировки")
    await callback.message.edit_text("Привет!", reply_markup=workouts_buttons)





