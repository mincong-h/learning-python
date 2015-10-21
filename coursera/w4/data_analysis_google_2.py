"""
get google's stock exchange data using matplotlib
"""
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date, datetime, timedelta
import pandas as pd

today = date.today()
start = today - timedelta(days=365)
quotes = quotes_historical_yahoo_ochl('GOOG', start, today)
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
# convert date format
dates = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x, '%Y-%m-%d')
    dates.append(y)
# set dates to index
quotesdf = pd.DataFrame(quotes, index=dates, columns=fields)
quotesdf = quotesdf.drop(['date'], axis=1)
# print
# print quotesdf
# print quotesdf[u'2014-12-02' : u'2014-12-09']
# print quotesdf.loc[1:5, ] # [row, col]
# print quotesdf.loc[:, ['low', 'volume']]
print quotesdf[(quotesdf.index>=u'2015-01-30') & (quotesdf.close>600)]
# group (example)
# g = tempdf.groupby('month')
# gvolume = g['volume']
# print gvolume.sum()
