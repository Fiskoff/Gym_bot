import asyncio
import logging

from aiogram import Bot, Dispatcher

from core.env_helper import env_helper
from routers.main_router import main_router

bot = Bot(env_helper.TOKEN)
dp = Dispatcher()


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())