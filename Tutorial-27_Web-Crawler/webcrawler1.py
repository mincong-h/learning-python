'''
Requirement: Python 3.4
'''


import urllib.request
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.thenewboston.com/trade/search.php?page=' + str(page)
        source_code = urllib.request.urlopen(url)
        print(source_code.read())
        plain_text = str(source_code.read)
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
            print(href)
        page += 1


trade_spider(10)
