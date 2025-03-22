from config import bot, CHANNEL_ID

from aiogram.types import FSInputFile

from unsplash_loader import UnsplashLoader


class TelegramPublisher:


    async def publish(self):
        loader = UnsplashLoader()

        if loader.get_random_image():

            photo_path = './tmp/photo.png'
            
            await bot.send_photo(chat_id=CHANNEL_ID, photo=FSInputFile(photo_path), caption="@everwalls")
            await bot.send_document(chat_id=CHANNEL_ID, document=FSInputFile(photo_path), caption="@everwalls")
        
        
        else:
            print("Failed to download image")