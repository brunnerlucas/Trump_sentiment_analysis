<h2>📥 How to Get the BTC CSV File</h2>
<p>To obtain Bitcoin price data, follow these steps:</p>

<h3>1️⃣ Install Dependencies</h3>
<p>Ensure you have <code>yfinance</code> installed:</p>
<pre><code>pip install yfinance</code></pre>

<h3>2️⃣ Download BTC Price Data Using Python</h3>
<p>Run the following script to download historical BTC prices and save them as a CSV file:</p>
<pre><code>
import yfinance as yf
import pandas as pd
btc_data = yf.download("BTC-USD", start="2016-01-01", end="2024-02-17")
btc_data.reset_index(inplace=True)
btc_data.to_csv("btc_price.csv", index=False)
print("BTC price data saved as btc_price.csv")

After running this script, btc_price.csv will be generated in the current directory.
