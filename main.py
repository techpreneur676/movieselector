import requests
from bs4 import BeautifulSoup
import random

response = requests.post("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text
data = BeautifulSoup(content, "html.parser")
heading = [i.get_text() for i in data.find_all("h3", class_="title")]
for i in range(len(heading)-1, 0, -1):
    with open("movies_name.txt",mode="a",encoding="utf-8") as new_file:
        new_file.write(f"{heading[i]}\n")


movie = random.choice(heading)
print(movie)
