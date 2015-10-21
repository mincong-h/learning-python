"""
get google's stock exchange data using matplotlib
"""
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date, timedelta
import pandas as pd

today = date.today()
start = today - timedelta(days=365)
quotes = quotes_historical_yahoo_ochl('GOOG', start, today)
quotesdf = pd.DataFrame(quotes)
print quotesdf
