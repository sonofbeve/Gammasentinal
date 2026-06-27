from flask import Flask
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def home():

    ticker = yf.Ticker("SMMT")

    try:
        price = ticker.fast_info["lastPrice"]
    except:
        price = "Unavailable"

    return f"""
    <h1>Gamma Sentinel</h1>
    <p><strong>Ticker:</strong> SMMT</p>
    <p><strong>Live Price:</strong> {price}</p>
    <p>Status: LIVE</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
