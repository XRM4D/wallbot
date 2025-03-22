import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


from dotenv import load_dotenv
load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

# Unsplash API
UNSPLASH_TOKEN = os.getenv("UNSPLASH_TOKEN")
