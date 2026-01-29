from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

build_counter = Counter('ue5_builds_total', 'Number of UE5 builds triggered')
health_counter = Counter('metrics_health_ping_total', 'Number of health pings')

@app.route('/')
def index():
    build_counter.inc()
    return "UE5 Build Triggered (simulated)!"

@app.route('/health')
def health():
    health_counter.inc()
    return {"status": "healthy"}

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
