import random
import logging
import requests

from config import UNSPLASH_TOKEN

logger = logging.getLogger(__name__)

class UnsplashLoader:

    def __get_random_query(self) -> str:
        with open("queries.txt", "r") as file:
            queries = file.readlines()
            query = random.choice(queries).strip()
            logger.info(f"Selected query: {query}")
            return query
        
    def __download_image(self, url: str, path: str = "./tmp/photo.png") -> None:
        logger.info(f"Downloading image from URL: {url}")
        with open(path, "wb") as file:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                file.write(img_data)
                logger.info("Image downloaded successfully.")
            else:
                logger.error(f"Failed to download image. Status code: {response.status_code}")
                raise Exception("Failed to download image")
    
    def get_random_image(self) -> bool:
        query = self.__get_random_query()
        url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_TOKEN}"
        response = requests.get(url).json()
        
        try:
            self.__download_image(response["urls"]["full"])
            logger.info("Image processing completed successfully.")
            return True
        except Exception as e:
            logger.error(f"Error during image processing: {e}")
            return False


