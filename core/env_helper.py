from os import getenv

from dotenv import load_dotenv


class HelperENV:
    load_dotenv()

    TOKEN = getenv("TG_TOKEN")
    DB_URL = getenv("DB_URL")


env_helper = HelperENV()
