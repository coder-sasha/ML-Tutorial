"""
This example demonstrates the work of a simple LSTM for predicting stock price.
The advantage of using NN for market data analysis is in abilities of NNs to can adapt to changing market conditions.
By it nature NNs use non-linear relationships and account for recent market data more heavily.
Hance NNs can to make better predictions than statistical models.

We implement forecasting NN in Python, using a LSTM-based NN model built with Google's TensorFlow framework.
The dataset covers the interval from 2020-01-01 to 2025-01-01.
We will see how LSTM-based model forecasts stock prices and make prediction of a market trend.
The LSTM model consists of the following 'parts':
 - 2 LSTM layers to capture long-term data dependencies;
 - 2 dropout layers to prevent overfitting;
 - a dense output layer (y) for results - price prediction;
"""

import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import warnings

# # supress unnecessary warnings from TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

warnings.filterwarnings('ignore')
# fetch stock data
symbol = 'MSFT'
df = yf.download(symbol, start="2020-01-01", end="2025-01-01")
print(df.head(10))

# calculate moving average (mean reversion baseline)
df["20_MA"] = df["Close"].rolling(window=20).mean()

# normalize market data
scaler = MinMaxScaler(feature_range=(0, 1))
df["Close_scaled"] = scaler.fit_transform(df["Close"].values.reshape(-1, 1))

# create data sequences for LSTM
seq_length = 50
X, Y = [], []
for i in range(len(df) - seq_length):
    X.append(df["Close_scaled"].iloc[i:i + seq_length].values)
    Y.append(df["Close_scaled"].iloc[i + seq_length])

X, Y = np.array(X), np.array(Y)

# Define LSTM model
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(units=50),
    Dropout(0.2),
    Dense(units=1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.summary()

# train the model
model.fit(X, Y, epochs=10, batch_size=32)

# make prediction of future prices
predictions = model.predict(X)

# convert predictions back to real price scale
predicted_prices = scaler.inverse_transform(predictions)

# plot results
plt.figure(figsize=(12, 6))
plt.plot(df.index[-len(predicted_prices):], df["Close"][-len(predicted_prices):], label="Real Price", color="blue")
plt.plot(df.index[-len(predicted_prices):], predicted_prices, label="Predicted Price", color="red")
plt.legend()
plt.title(f"LSTM Price Predictions for {symbol}")
plt.show()

print("\n   :)")
