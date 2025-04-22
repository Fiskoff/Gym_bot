from os import getenv

from dotenv import load_dotenv


class HelperENV:
    load_dotenv()

    TOKEN = getenv("BOT_TOKEN")
    DB_URL = getenv("DB_URL")


env_helper = HelperENV()
