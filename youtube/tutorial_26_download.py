#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Tutorial's name : Python Programming Tutorial - 24 - Downloading Files from the Web
Tutorial's link : https://www.youtube.com/watch?v=MjwWzBiAMck&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=24
'''

from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=4&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

# definition
def download_stock_data(csv_url) :
  response = request.urlopen(csv_url)
  csv = response.read()
  csv_str = str(csv)
  rows = csv_str.split("\\n")
  dest_url = r'/Users/huangmincong/desktop/goog.csv' # destion file's name for Mac
  fx = open(dest_url, "w")
  for row in rows :
    fx.write(row + "\n")
    print(row)
  fx.close()

# execution
download_stock_data(goog_url)
print("END")
input("press<enter>")
