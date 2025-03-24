<h2>📥 How to Get the BTC CSV File</h2>
<p>To obtain Bitcoin price data, download the following:</p>
<p>🔗 <a href="https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data">Bitcoin Historical Data (Kaggle)</a></p>

<h2>📥 How we Collected Trump's Tweets</h2>
<p>The tweets related to <b>Bitcoin, cryptocurrency, blockchain, and financial policies</b> were downloaded from:</p>
<p>🔗 <a href="https://www.thetrumparchive.com/?resultssortOption=%22Latest%22">The Trump Archive</a></p>

<p>The search terms used to filter relevant tweets include:</p>
<ul>
  <li>"Bitcoin" | "BTC" | "Crypto" | "Cryptocurrency" | "Blockchain" | "Digital currency" | "Ethereum" | "coin" | "Stablecoin" | "Mining" | "XRP" | "Libra" | "Stimulus" | "Interest Rate" | "Altcoin" | "DeFi" | "Web3" | "NFT" | "Smart Contract" | "Tokenomics" | "Layer 2 Scaling" | "Metaverse" | "CBDC" | "HODL" | "FUD" | "FOMO" | "Bull Run" | "Bear Market" | "Whale" | "Pump and Dump" | "Mooning" | "Airdrop" | "DEX" | "CEX" | "Federal Reserve" | "Monetary Policy" | "Inflation" | "Deflation" | "Recession" | "GDP Growth" | "Unemployment Rate" | "Stock Market Crash" | "Hedge Fund" | "Bailout" | "Debt Ceiling" | "Yield Curve" | "Fiat Currency" | "Quantitative Easing" | "Gold Standard" | "Reserve Currency" | "SEC" | "CFTC" | "Regulation" | "Crypto Ban" | "Taxation" | "Legal Tender" | "Stablecoin Regulation" | "AML" | "KYC" | "Crypto Crackdown" | "AI Trading Bots" | "Machine Learning in Finance" | "Quantum Computing in Crypto" | "Zero-Knowledge Proofs" | "Privacy Coins" | "Darknet Markets" | "5G & Crypto Adoption" | "Internet of Value" | "Tokenized Assets" | "Digital Identity"</li>
</ul>
<a href="https://data.page/json/csv">Use this link tor transform the json to csv!

<h2>📥 How to Get the Fear and Greed Index CSV File</h2>
<p>To obtain the Fear and Greed Index download the following</p>
<p>🔗 <a href="https://www.kaggle.com/datasets/adilbhatti/bitcoin-and-fear-and-greed"> Fear and greed Index download </a></p>


<hr>

<h2>⚙️ Kafka Setup</h2>

<h3>📄 List All Kafka Topics</h3>
<pre><code>kafka-topics.sh --list --bootstrap-server localhost:9092</code></pre>

<h3>🧱 Create <code>btc_price</code> Topic</h3>
<p>If there is no topic called <code>btc_price</code>, create one with:</p>
<pre><code>kafka-topics.sh --create --topic btc_price --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1</code></pre>

<hr>

<h2>🚀 Running the API</h2>

<h3>📂 Step 1: Change Directory</h3>
<pre><code>cd path/to/your/api</code></pre>

<h3>🐍 Step 2: Create and Activate Virtual Environment</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>

<h3>📦 Step 3: Install Libraries</h3>
<pre><code>pip install pandas flask deltalake</code></pre>

<p>Then you're ready to run the API!</p>
