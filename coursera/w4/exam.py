import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
start = datetime(2014,1,1)
end = datetime(2014,12,31)
quotesMS14 = quotes_historical_yahoo_ochl('MSFT', start, end)
fields = ['date','open','close','high','low','volume']
list1 = []
for i in range(0,len(quotesMS14)):
    x = date.fromordinal(int(quotesMS14[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
#print list1
quotesdfMS14 = pd.DataFrame(quotesMS14, index = list1, columns = fields)
#print quotesMS14
listtemp1 = []
for i in range(0,len(quotesdfMS14)):
    temp = time.strptime(quotesdfMS14.index[i],"%Y-%m-%d")
    listtemp1.append(temp.tm_mon)
#print listtemp1
quotesdfMS14['month'] = listtemp1
#print quotesdfMS14
#closemaxINTC = quotesdfMS14.groupby('month').max().close
openMS = quotesdfMS14.groupby('month').mean().open
listopen = []
for i in range(1, 13):
    listopen.append(openMS[i])
#---
#plt.plot(openMS.index, openMS.values, '-.*r')
#---
#plt.plot(openMS.index, listopen)
#plt.xlabel('Month')
#plt.ylabel('Average Open Price')
#plt.title('Stock Statistics of Microsoft')
#---
#openMS.plot(grid=True)
quotesdfMS14 = quotesdfMS14['2014-01-01':'2015-01-01']
openMS2 = quotesdfMS14.open.plot()
plt.show()

