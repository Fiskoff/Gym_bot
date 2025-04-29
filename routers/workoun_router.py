from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from routers.keyboard import workout_button, inline_workouts
from routers.workout_fsm_router import workout_fsm_router
from services.exercise_services import get_exercise_for_workout_service
from services.workout_services import get_id_workout_service


workout_router = Router()
workout_router.include_router(workout_fsm_router)


@workout_router.message(F.text == "Тренировка")
async def callback_workouts(message: Message):
    await message.answer(text="Раздел с тренировками", reply_markup=workout_button)


@workout_router.callback_query(F.data == "workouts")
async def callback_workouts(callback: CallbackQuery):
    await callback.answer("Выбрали тренировки")
    await callback.message.edit_text("Ваши тренировки", reply_markup=await inline_workouts(callback.from_user.id))


@workout_router.callback_query(F.data)
async def handle_workout_callback(callback: CallbackQuery):
    workout_data = callback.data.split('|')
    workout_name, workout_date = workout_data
    await callback.answer(f"Вы выбрали тренировку: {workout_name} на дату: {workout_date}")
    workout_id = await get_id_workout_service(workout_name, workout_date)
    exercises_dict = await get_exercise_for_workout_service(workout_id)
    await callback.message.answer(f"Информация о тренировке:\nНазвание: {workout_name}\nДата: {workout_date}")

    message_list = []
    for exercise_dict in exercises_dict:
        temp_str = (f"{exercise_dict['exercise_id']}) {exercise_dict['exercise_name']}\n"
                    f"Количество подходов: {exercise_dict['sets']}\n"
                    f"Количество повторений: {exercise_dict['reps']}\n"
                    f"Рабочий вес: {exercise_dict['weight']}\n"
                    f"\n")
        message_list.append(temp_str)

    await callback.message.answer(''.join(message_list))






