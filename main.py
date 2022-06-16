import logging

from pyrogram import Client, idle

from Config import *

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


logging.getLogger("pyrogram").setLevel(logging.WARNING)
app = Client(
    "Basic Döviz Botu",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="BasicDovizBot"),
)

app.start()
print("Bot başlatıldı.")
idle()
