import random
import logging
import requests
from PIL import Image
import os

from config import UNSPLASH_TOKEN

logger = logging.getLogger(__name__)

class UnsplashLoader:

    def __get_random_query(self) -> str:
        with open("queries.txt", "r") as file:
            queries = file.readlines()
            query = random.choice(queries).strip()
            logger.info(f"Selected query: {query}")
            return query
        
    def __convert_to_16_9(self, path: str) -> None:
        logger.info(f"Converting image to 16:9 format: {path}")
        try:
            with Image.open(path) as img:
                width, height = img.size
                target_width = width
                target_height = int(width * 9 / 16)

                if target_height > height:
                    target_height = height
                    target_width = int(height * 16 / 9)

                left = (width - target_width) / 2
                top = (height - target_height) / 2
                right = (width + target_width) / 2
                bottom = (height + target_height) / 2

                cropped_img = img.crop((left, top, right, bottom))
                cropped_img.save(path)
                logger.info("Image successfully converted to 16:9 format.")
        except Exception as e:
            logger.error(f"Failed to convert image to 16:9 format: {e}")
            raise

    def __ensure_file_size(self, path: str, max_size_mb: int = 10) -> None:
        logger.info(f"Checking if image size exceeds {max_size_mb} MB...")
        try:
            while os.path.getsize(path) > max_size_mb * 1024 * 1024:
                logger.info(f"Image size exceeds {max_size_mb} MB. Cropping...")
                with Image.open(path) as img:
                    width, height = img.size
                    cropped_img = img.crop((0, 0, width - 100, height - 100))  # Crop 100px from each side
                    cropped_img.save(path)
                    logger.info("Image cropped to reduce size.")
            logger.info("Image size is within the acceptable limit.")
        except Exception as e:
            logger.error(f"Failed to ensure image size: {e}")
            raise

    def __download_image(self, url: str, path: str = "./tmp/photo.png") -> None:
        logger.info(f"Downloading image from URL: {url}")
        with open(path, "wb") as file:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                file.write(img_data)
                logger.info("Image downloaded successfully.")
                self.__convert_to_16_9(path)
                self.__ensure_file_size(path)
            else:
                logger.error(f"Failed to download image. Status code: {response.status_code}")
                raise Exception("Failed to download image")
    
    def get_random_image(self) -> bool:
        query = self.__get_random_query()
        url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_TOKEN}"
        response = requests.get(url).json()
        
        try:
            self.__download_image(response["urls"]["full"])
            logger.info("Image processing completed successfully.")
            return True
        except Exception as e:
            logger.error(f"Error during image processing: {e}")
            return False


