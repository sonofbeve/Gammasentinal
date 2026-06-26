from flask import Flask
import os
import requests

app = Flask(__name__)

# Get API key from Render environment variables
API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():

    # If API key is missing, show error clearly
    if not API_KEY:
        return "<h1>ERROR</h1><p>Missing API_KEY in Render environment variables</p>"

    url = "https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/SMMT"
    params = {"apiKey": API_KEY}

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
    except Exception as e:
        return f"<h1>REQUEST ERROR</h1><pre>{str(e)}</pre>"

    # Show FULL response first (no guessing, no parsing errors)
    return f"""
    <h1>SMMT SENTINEL</h1>
    <h2>RAW DATA (debug mode)</h2>
    <pre>{data}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
