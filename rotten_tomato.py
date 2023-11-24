from bs4 import BeautifulSoup
import requests

url="https://www.rottentomatoes.com/browse/movies_in_theaters/critics:certified_fresh"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movie_list=soup.find("div", class_="discovery-tiles__wrap")
movie_list_divs=movie_list.find_all("div", class_="js-tile-link")
for movie in movie_list_divs:
    name=movie.find("span", class_="p--small").text.strip()
    score=movie.find("score-pairs-deprecated")["criticsscore"]
    print(name,score)
