from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State

from routers.keyboard import create_exercise_button
from services.exercise_services import create_new_exercise
from services.workout_services import get_last_workout_service


class ExerciseFSM(StatesGroup):
    name_exercise = State()
    sets = State()
    reps = State()
    weight = State()


exercise_fsm_router = Router()


@exercise_fsm_router.callback_query(F.data == "yes_create_exercise")
async def start_create_exercise(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Добавление упражнения")
    await state.set_state(ExerciseFSM.name_exercise)
    await callback.message.answer("Введите название упражнения")


@exercise_fsm_router.message(ExerciseFSM.name_exercise)
async def process_exercise_name(message: Message, state: FSMContext):
    await state.update_data(name_exercise=message.text)
    await state.set_state(ExerciseFSM.sets)
    await message.answer("Укажите количество подходов")


@exercise_fsm_router.message(ExerciseFSM.sets)
async def process_exercise_sets(message: Message, state: FSMContext):
    await state.update_data(sets=message.text)
    await state.set_state(ExerciseFSM.reps)
    await message.answer("Укажите количество повторений")


@exercise_fsm_router.message(ExerciseFSM.reps)
async def process_exercise_reps(message: Message, state: FSMContext):
    await state.update_data(reps=message.text)
    await state.set_state(ExerciseFSM.weight)
    await message.answer("Укажите вес на снаряде")


@exercise_fsm_router.message(ExerciseFSM.weight)
async def process_exercise_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    workout_id = await get_last_workout_service(message.from_user.id)
    await create_new_exercise(
        workout_id, data["name_exercise"], int(data["sets"]), int(data["reps"]), int(data["weight"])
    )
    await message.answer("Упражнение добавлено\nДобавим ещё упражнение?", reply_markup=create_exercise_button)
    await state.clear()


@exercise_fsm_router.callback_query(F.data == "no_create_exercise")
async def cancel_create_exercise(callback: CallbackQuery):
    await callback.answer("Тренировка сохранена")
