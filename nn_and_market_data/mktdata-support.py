
import pandas as pd
import yfinance as yf
import mplfinance as mpf
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# fetch 1 year of dailt ticks
symbol = 'MSFT'
data = yf.download(symbol, period='1y', interval='1d') 

# select 'Close' price and scale it
closing_prices = data['Close'].values.reshape(-1, 1)

# plotting the actual data
plt.figure(figsize=(10,6))
plt.plot(data.index[-60:], data['Close'][-60:], linestyle='-', marker='o', color='black')

plt.title(f"Daily {symbol} Stock Price")
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()