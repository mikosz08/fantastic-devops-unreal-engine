from flask import Flask, render_template, request
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

BUILD_COUNTER = Counter('ue5_builds_total', 'Number of UE5 builds triggered')
HEALTH_COUNTER = Counter('health_checks_total', 'Total /health checks calls')

HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"],
)


@app.route('/')
def index():
    return "Hello UE5 Metrics Server! Visit /build to simulate a UE5 build or /health for health checks."

@app.route('/build')
def build():
    BUILD_COUNTER.inc()
    return "UE5 Build Triggered (simulated)!"

@app.route('/health')
def health():
    HEALTH_COUNTER.inc()
    health_count = HEALTH_COUNTER._value.get()
    print(f"Health check called. Total visits: {health_count}")
    return render_template("health.html", visits=int(health_count))

@app.after_request
def count_requests(response):
    HTTP_REQUESTS_TOTAL.labels(method=request.method,
                               endpoint=request.path,
                               status=str(response.status_code),
    ).inc()
    return response

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
    print("Metrics Server Down. Exiting.")
