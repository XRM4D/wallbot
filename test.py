from pyunsplash import PyUnsplash
import requests
import logging

pyunsplash = PyUnsplash(api_key="n1obS5wmgRVyeQ2t6zV9itJLYncGHqmFigzfktkOV9g")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Sending request to Unsplash API...")
response = requests.get("https://api.unsplash.com/photos/random?query=texture&orientation=landscape&client_id=n1obS5wmgRVyeQ2t6zV9itJLYncGHqmFigzfktkOV9g").json()

logger.info("Writing image to file...")
with open(f"./unsplash_en/photo.png", "wb") as file:
    img_data = requests.get(response["urls"]["full"]).content
    file.write(img_data)
    logger.info("Image saved successfully.")