Bitcoin Price & Trump Tweets Dataset

This repository contains:

Bitcoin Price Data (btc_price.csv) – Historical BTC price data obtained using yfinance.

Trump Tweets Dataset (trump_tweets.csv) – A dataset of Donald Trump's tweets related to Bitcoin, cryptocurrency, and financial topics.

📥 How to Get the BTC CSV File

To obtain Bitcoin price data, follow these steps:

1️⃣ Install Dependencies

Ensure you have yfinance installed:

pip install yfinance

2️⃣ Download BTC Price Data Using Python

Run the following script to download historical BTC prices and save them as a CSV file:

import yfinance as yf
import pandas as pd

# Download BTC price data
btc_data = yf.download("BTC-USD", start="2016-01-01", end="2024-02-17")

# Reset index to make 'Date' a column
btc_data.reset_index(inplace=True)

# Save as CSV
btc_data.to_csv("btc_price.csv", index=False)
print("BTC price data saved as btc_price.csv")

After running this script, btc_price.csv will be generated in the current directory.

📥 How I Collected Trump's Tweets

The tweets related to Bitcoin, cryptocurrency, blockchain, and financial policies were downloaded from:
🔗 The Trump Archive

The search terms used to filter relevant tweets include:

"Bitcoin", "BTC", "Crypto", "Cryptocurrency"

"Blockchain", "Digital currency", "Ethereum"

"Coin", "Stablecoin", "Mining", "XRP"

"Libra", "Stimulus", "Interest Rate"

