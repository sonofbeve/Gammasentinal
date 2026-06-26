from flask import Flask
import requests

app = Flask(__name__)

import os
API_KEY = os.getenv("API_KEY")

def get_price():
    url = f"https://api.polygon.io/v2/last/trade/SMMT?apiKey={API_KEY}"
    r = requests.get(url).json()
    return str(r)

    try:
        return r["results"]["p"]
    except:
        return "N/A"

@app.route("/")
def home():
    price = get_price()

    return f"""
    <h1>SMMT SENTINEL v2</h1>
    <p>Live Price: {price}</p>
    <p>Status: LIVE</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
