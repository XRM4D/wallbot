import random

import requests

from config import UNSPLASH_TOKEN

class UnsplashLoader:

    def __get_random_query(self) -> str:
        with open("queries.txt", "r") as file:
            queries = file.readlines()
            return random.choice(queries).strip()
        
    def __download_image(self, url: str, path: str = "./tmp/photo.png") -> None:
        with open(path, "wb") as file:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                file.write(img_data)
            else:
                raise Exception("Failed to download image")
    
    def get_random_image(self) -> bool:
        query = self.__get_random_query()
        url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_TOKEN}"
        response = requests.get(url).json()
        
        try:
            self.__download_image(response["urls"]["full"])
            return True
        except Exception:
            return False


        