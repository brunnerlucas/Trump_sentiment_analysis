<h2>📥 How to Get the BTC CSV File</h2>
<p>To obtain Bitcoin price data, download the following:</p>
<p>🔗 <a href="https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data">Bitcoin Historical Data (Kaggle)</a></p>

<h2>📥 How I Collected Trump's Tweets</h2>
<p>The tweets related to <b>Bitcoin, cryptocurrency, blockchain, and financial policies</b> were downloaded from:</p>
<p>🔗 <a href="https://www.thetrumparchive.com/?resultssortOption=%22Latest%22">The Trump Archive</a></p>

<p>The search terms used to filter relevant tweets include:</p>
<ul>
"Bitcoin" | "BTC" | "Crypto" | "Cryptocurrency" | "Blockchain" | "Digital currency" | "Ethereum" | "coin" | "Stablecoin" | "Mining" | "XRP" | "Libra" | "Stimulus" | "Interest Rate" | "Altcoin" | "DeFi" | "Web3" | "NFT" | "Smart Contract" | "Tokenomics" | "Layer 2 Scaling" | "Metaverse" | "CBDC" | "HODL" | "FUD" | "FOMO" | "Bull Run" | "Bear Market" | "Whale" | "Pump and Dump" | "Mooning" | "Airdrop" | "DEX" | "CEX" | "Federal Reserve" | "Monetary Policy" | "Inflation" | "Deflation" | "Recession" | "GDP Growth" | "Unemployment Rate" | "Stock Market Crash" | "Hedge Fund" | "Bailout" | "Debt Ceiling" | "Yield Curve" | "Fiat Currency" | "Quantitative Easing" | "Gold Standard" | "Reserve Currency" | "SEC" | "CFTC" | "Regulation" | "Crypto Ban" | "Taxation" | "Legal Tender" | "Stablecoin Regulation" | "AML" | "KYC" | "Crypto Crackdown" | "AI Trading Bots" | "Machine Learning in Finance" | "Quantum Computing in Crypto" | "Zero-Knowledge Proofs" | "Privacy Coins" | "Darknet Markets" | "5G & Crypto Adoption" | "Internet of Value" | "Tokenized Assets" | "Digital Identity"
</ul>

<h2>⚙️ Kafka Setup</h2>

<h3>📄 List All Kafka Topics</h3>

To view all existing Kafka topics, run the following command:

kafka-topics.sh --list --bootstrap-server localhost:9092
<h3>🧱 Create <code>btc_price</code> Topic</h3>
If there is no topic called btc_price, create one with:
<ul>
kafka-topics.sh --create --topic btc_price --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
</ul>
<h2>🚀 Running the API</h2> <h3>📂 Step 1: Change Directory</h3>
Navigate to the directory where your API code is saved:
<ul>
cd path/to/your/api
</ul>
<h3>🐍 Step 2: Create and Activate Virtual Environment</h3>
<ul>
python3 -m venv venv
source venv/bin/activate
</ul>
<h3>📦 Step 3: Install Requirements</h3>
<ul>
pip install pandas flask deltalake
</ul>


