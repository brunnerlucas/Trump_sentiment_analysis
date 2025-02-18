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
</code></pre>

After running this script, btc_price.csv will be generated in the current directory.

<hr>

<h2>📥 How I Collected Trump's Tweets</h2>
<p>The tweets related to <b>Bitcoin, cryptocurrency, blockchain, and financial policies</b> were downloaded from:</p>
<p>🔗 <a href="https://www.thetrumparchive.com/?searchbox=%22%5C%22Bitcoin%5C%22+%7C+%5C%22BTC%5C%22+%7C+%5C%22Crypto%5C%22+%7C+%5C%22Cryptocurrency%5C%22+%7C+%5C%22Blockchain%5C%22+%7C+%5C%22Digital+currency%5C%22+%7C+%5C%22Ethereum%5C%22++%7C+%5C%22coin%5C%22+%7C+%5C%22Stablecoin%5C%22+%7C+%5C%22Mining%5C%22+%7C+%5C%22XRP%5C%22++%7C+%5C%22Libra%5C%22++%7C+%5C%22Stimulus%5C%22++%7C+%5C%22Interest+Rate%5C%22%22&resultssortOption=%22Latest%22">The Trump Archive</a></p>

<p>The search terms used to filter relevant tweets include:</p>
<ul>
    <li>"Bitcoin", "BTC", "Crypto", "Cryptocurrency"</li>
    <li>"Blockchain", "Digital currency", "Ethereum"</li>
    <li>"Coin", "Stablecoin", "Mining", "XRP"</li>
    <li>"Libra", "Stimulus", "Interest Rate"</li>
</ul>

