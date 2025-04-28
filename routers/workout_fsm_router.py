from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from services.workout_services import create_new_workout
from routers.keyboard import create_exercise_button


class WorkoutFSM(StatesGroup):
    name_workout = State()
    workout_date = State()


workout_fsm_router = Router()


@workout_fsm_router.callback_query(F.data == "create_workout")
async def start_create_workout(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Создание тренировки")
    await callback.message.answer("Создание новой тренировки")
    await state.set_state(WorkoutFSM.name_workout)
    await callback.message.answer("Введите название тренировки")


@workout_fsm_router.message(WorkoutFSM.name_workout)
async def process_workout_name(message: Message, state: FSMContext):
    await state.update_data(name_workout=message.text)
    await state.set_state(WorkoutFSM.workout_date)
    await message.answer("Введите дату тренировки")


@workout_fsm_router.message(WorkoutFSM.workout_date)
async def process_workout_date(message: Message, state: FSMContext):
    await state.update_data(workout_date=message.text)
    data = await state.get_data()
    await create_new_workout(message.from_user.id, data["workout_date"], data["name_workout"])
    await message.answer("Тренировка создана\nДобавим в неё упражнений?", reply_markup=create_exercise_button)
    await state.clear()