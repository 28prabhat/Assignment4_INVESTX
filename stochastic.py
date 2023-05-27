import pandas as pd
import numpy as np
import yfinance as yf
from ta import trend
import matplotlib.pyplot as plt
data = yf.download("AAPL", start="2023-01-01", end="2023-05-01")
df = data.reset_index()
#%K = [(Current Closing Price - Lowest Low) / (Highest High - Lowest Low)] * 100
list=[]

for i in range(81):
    close=df['Close'][i]
    low=df['Low'][i]
    high=df['High'][i]
    k=(close-low)/(high-low)
    list.append(k)

df['%K']=list
df['SMA'] = trend.sma_indicator(df['%K'], window=3)


df.plot(x='Date',y=['%K','SMA'])
df.plot(x='Date',y='Open')        
        
plt.show()
