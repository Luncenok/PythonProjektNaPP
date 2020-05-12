from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

print("Witaj w programie do sprawdzania temperatury na dzisiaj!")
print("Podaj miejscowość bez polskich znaków: ")
url = "https://meteoprog.pl/pl/weather/"
miejscowosc = input()
url += miejscowosc

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.find_all(attrs={"itemprop": "title"})
temperatura = soup.find(class_="temperature_value")
pogodaszczegoly = soup.find(class_="icon-weather")
print(title[len(title)-1].get_text() + ": " + temperatura.get_text() + " stopni Celscjusza - " + pogodaszczegoly['title'])
