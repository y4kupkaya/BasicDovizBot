from dotenv import load_dotenv
from os import getenv
load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME")
