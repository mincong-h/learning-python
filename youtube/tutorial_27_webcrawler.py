'''
Python 3.4
'''

import urllib.request
from bs4 import BeautifulSoup


def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    # code loading
    url = 'https://www.thenewboston.com/trade/search.php?page=' + str(page)
    source_code = urllib.request.urlopen(url)
    plain_text = source_code.read()
    # transformation
    soup = BeautifulSoup(plain_text)
    # get links
    for link in soup.find_all('a'):
      href = link.get('href')
      if href[:4] != 'http':
        if href[0] == '/':
          url_complete = url + href
        else:
          url_complete = url + '/' + href
      else:
        url_complete = url
      print(url_complete)
      # next page
      page += 1


trade_spider(10)
