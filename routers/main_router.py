from aiogram import Router

from routers.user_router import user_router


main_router = Router()

main_router.include_router(user_router)