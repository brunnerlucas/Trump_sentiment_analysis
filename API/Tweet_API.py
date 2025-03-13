from flask import Flask, jsonify
import pandas as pd
import random
from deltalake import DeltaTable  # Delta Lake Python API

app = Flask(__name__)

HDFS_PATH = "hdfs://localhost:9000/lakehouse/silver/trump_btc/trump"

def load_data():
    """Load Delta table directly into Pandas DataFrame"""
    try:
        # Read Delta table into Pandas
        df = DeltaTable(HDFS_PATH).to_pandas()
        return df
    except Exception as e:
        print(f"Error loading Delta table: {e}")
        return None

# Load Data at Startup
data_df = load_data()

@app.route('/random-tweet', methods=['GET']) #endpoint
def get_random_tweet():
    global data_df
    
    if data_df is None or data_df.empty:
        return jsonify({"error": "No data available"}), 404

    # Select a random tweet
    random_tweet = data_df.sample(n=1).to_dict(orient="records")[0]
    
    return jsonify(random_tweet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=28881)  # Adjust port as needed




#curl http://localhost:28881/random-tweet  to get the api response in the terminal
# run the virtual env all dependencies installed there: source venv/bin/activate
#run the api but needs to be in the right directory:  python3 Tweet_API.py




