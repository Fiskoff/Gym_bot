from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services.workout_services import get_all_workouts

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Тренировка"), KeyboardButton(text="Прогресс")],],
    resize_keyboard=True,
    input_field_placeholder="Выбери пункт меню"
)


workout_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Тренировки", callback_data="workouts")],
        [InlineKeyboardButton(text="Создать тренировку", callback_data="create_workout")],
        [InlineKeyboardButton(text="Изменить тренировку", callback_data="update_workout")],
        [InlineKeyboardButton(text="Удалить тренировку", callback_data="delete_workout")],
    ]
)


async def inline_workouts(user_id: int):
    workouts = await get_all_workouts(user_id)
    new_workouts_buttons = InlineKeyboardBuilder()
    for workout in workouts:
        new_workouts_buttons.add(InlineKeyboardButton(text=workout, callback_data=workout))
    return new_workouts_buttons.adjust(2).as_markup()


create_exercise_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data="yes_create_exercise"),
        InlineKeyboardButton(text="Нет", callback_data="no_create_exercise")],
    ]
)