import pandas as pd
import matplotlib.pyplot as plt

# Read stock price dataset from CSV file
df = pd.read_csv('Plotando/btc-usd-max.csv')

# Extract stock prices from the dataframe
stock_prices = df['price'].tolist()

# Plotting the histogram
plt.hist(stock_prices, bins=10, edgecolor='black')

# Adding labels and title
plt.xlabel('Stock Prices')
plt.ylabel('Frequency')
plt.title('Stock Price Histogram')

# Displaying the histogram
plt.show()