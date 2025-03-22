from pyunsplash import PyUnsplash
import requests

pyunsplash = PyUnsplash(api_key="n1obS5wmgRVyeQ2t6zV9itJLYncGHqmFigzfktkOV9g")



response = requests.get("https://api.unsplash.com/photos/random?query=texture&orientation=landscape&client_id=n1obS5wmgRVyeQ2t6zV9itJLYncGHqmFigzfktkOV9g").json()
with open(f"./unsplash_en/photo.png", "wb") as file:
    img_data = requests.get(response["urls"]["full"]).content
    file.write(img_data)