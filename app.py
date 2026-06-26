from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>SMMT SENTINEL v1</h1><p>Status: LIVE</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
