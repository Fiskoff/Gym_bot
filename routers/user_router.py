from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from services.user_services import create_new_user
from routers.keyboard import main_keyboard


user_router = Router()


@user_router.message(CommandStart())
async def create_user(message: Message):
    result = await create_new_user(message.from_user.id, message.from_user.first_name)
    await message.answer(text=f"Hello!, {message.from_user.first_name}\n{result}", reply_markup=main_keyboard)
