from flask import Flask
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def home():

    ticker = yf.Ticker("SMMT")

    try:
        info = ticker.fast_info

        price = info.get("lastPrice", "Unavailable")
        previous = info.get("previousClose")

        if isinstance(price, (int, float)) and isinstance(previous, (int, float)):
            change = price - previous
            percent = (change / previous) * 100
        else:
            change = "N/A"
            percent = "N/A"

    except Exception:
        price = "Unavailable"
        change = "N/A"
        percent = "N/A"

    return f"""
    <h1>Gamma Sentinel</h1>

    <h2>SMMT</h2>

    <p><strong>Live Price:</strong> {price}</p>
    <p><strong>Today's Change:</strong> {change}</p>
    <p><strong>Percent Change:</strong> {percent}</p>

    <hr>

    <p>Status: LIVE</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
