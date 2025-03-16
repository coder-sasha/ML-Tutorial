**Neural Networks for Market Data**
Predicting stock market moves and trends has always been a great challenge for investors, professional traders and scientists.   
(remember the story of Sir Issac Newton lost money, entering tulips market).   
Stock prices are influenced by many unpredictable factors:  
- change of economic indicators;  
- global and local news;  
- political events;  
- even chats in social networks – the GameStop story;   

Can neural networks enhance stock market predictions?   
Stock prices are time series. NN takes this time series data as input and learns how to predict future movements.  
In financial markets, patterns are key. Traders study and seek monthly, daily, hourly patterns to make decisions about trading actions.  
And pattern recognition is the area where neural networks really do well.  
Traditional models like linear regression or ARIMA seek linear relationships, and due to the complexity of the stock market this is not a good approach.  
Neural networks, on the other hand, are meant to detect non-linear patterns.  
Using neural networks, we can analyze high-dimensional data and add more data to analysis: such as social media sentiment, news headlines, and even account for influence of political decisions.  
In our example we use show how to use **LSTM** - Long Short-Term Memory network that are good fit for capturing long-term dependencies in time-series.  
Run the example, see results, use different instruments, experiment with the network structure (add or remove layers).  
