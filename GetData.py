import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader .data as web

style.use('ggplot')

start = dt.datetime(2000,1,1) 
end = dt.datetime(2020,12,31)

df = web.DataReader('DMART.NS','yahoo',start,end)
print(df.head())
df.to_csv('DMART.csv')

df= pd.read_csv('DMART.csv',parse_dates = True , index_col=0)
