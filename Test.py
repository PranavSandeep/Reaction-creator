from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_game_engines'
content = requests.get(URL)

soup = BeautifulSoup(content.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
