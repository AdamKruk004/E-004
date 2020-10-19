import requests
from bs4 import BeautifulSoup

url = 'https://kantoronline.pl/kursy-walut'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
body = soup.body
table = body.find('table', {'id': 'tableofcurrency'})

usd: int = table.find('td', {'id': 'usdsell'}).text
eur: int = table.find('td', {'id': 'eursell'}).text
gbp: int = table.find('td', {'id': 'gbpsell'}).text
pln = 1.0000

print(usd, eur, gbp, sep="\n")
