import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.x-rates.com/table/?from=USD&amount=1')
soup = BeautifulSoup(page.content, 'html.parser')
chart = soup.find(id = 'content')
currency_table = chart.find_all('tr')

currency= {}
currency_usdrates = {}

for tr in currency_table:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if row:
        currency[row[0]] = float(row[1])
        currency_usdrates[row[0]] = float(row[2])
