from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "message": "DevOps Diploma Project"
    })

@app.route("/health")
def health():
    REQUEST_COUNT.inc()
    return jsonify({
        "status": "UP"
    })

@app.route("/version")
def version():
    REQUEST_COUNT.inc()
    return jsonify({
        "version": "1.0.0"
    })

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)