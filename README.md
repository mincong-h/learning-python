# Python-Programming-Exercises
I'm learning Python by following the <b>Python Programming Tutorials</b> and <b>Python 3.4 Programming Tutorials</b> on YouTube, created by <b>thenewboston</b>. Here are the links :
<ul>
  <li>Python 3.4 Programming Tutorials <br>https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_ </li>
  <li>Python Programming Tutorials <br>https://www.youtube.com/playlist?list=PLEA1FEF17E1E5C0DA </li>
</ul>
During these tutorials, I've leant many things. Thanks a lot to Bucky!!! He really did a good job!!! Actually, there're somethings particularly interesting, which I want to share with you. Including : 
<ul>
  <li>Downloading Files from the Web</li>
</ul>

## Program 1 : Downloading Files from the Web
At the <b>Tutorial-26_Downloading-Files-from-the-Web</b>, Bucky taught us how to get a csv file from the internet.<br>
You can check the video here : https://www.youtube.com/watch?v=MjwWzBiAMck&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=24. <br>
The principle steps of the program are : Start -> send a request -> read the result -> data stocking -> printf -> End.

### Source code
```python
def download_stock_data(csv_url) :
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    rows = csv_str.split("\\n")
    dest_url = r'/Users/mincong-h/desktop/goog.csv' # destion file's name for Mac
    fx = open(dest_url, "w")
    for row in rows :
        fx.write(row + "\n")
        print(row)
    fx.close()
```

## Program 2 : Web Crawler
### Requirement and installation(for Mac)
This webcrawler is using the <a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/"><b>beautifulsoup4</b></a> module.<br> You need to download it from the internet, then release it.
When the files has been released successfully, you need to install this module. For Mac user, you can install the <a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/"><b>beautifulsoup4</b></a> by using the Terminal command : entre the file's path by the <code>cd</code> command, then use <code>sudo python3.4 ./setup.py install</code> to install.<br> For more informations, here are some useful links :<br>
<ul>
  <li><a href="https://www.youtube.com/watch?v=XjNm9bazxn8&index=25&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_">Python Programming Tutorial - 25 - How to Build a Web Crawler (1/3)</a></li>
  <li><a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup">Installing Beautiful Soup</a></li>
  <li><b>#CN </b><a href="http://www.jackman.cn/?p=980">在MAC 中安装BEAUTIFULSOUP FOR PYTHON3.3</a></li>
</ul>

### Source code
```python
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
            print(href)
        # next page
        page += 1


trade_spider(2)
```
