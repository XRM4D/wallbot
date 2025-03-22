import os
import logging

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

# Unsplash API
UNSPLASH_TOKEN = os.getenv("UNSPLASH_TOKEN")

if BOT_TOKEN and CHANNEL_ID and UNSPLASH_TOKEN:
    logger.info("Environment variables loaded successfully.")
else:
    logger.error("Missing one or more required environment variables.")
