from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



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

workouts_buttons = InlineKeyboardMarkup(
inline_keyboard=[
        [InlineKeyboardButton(text="25.01.25", callback_data="25.01.25")],
        [InlineKeyboardButton(text="28.01.25", callback_data="28.01.25")],
        [InlineKeyboardButton(text="30.01.25", callback_data="30.01.25")],
        [InlineKeyboardButton(text="1.02.26", callback_data="1.02.26")],
    ]
)