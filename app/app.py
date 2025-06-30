from prometheus_client import start_http_server, Summary, Counter, Gauge
import time
import requests

# Prometheus metrics
REQUEST_TIME = Summary('google_request_duration_seconds', 'Time spent requesting Google')
REQUEST_COUNTER = Counter('google_request_count', 'Total number of requests to Google')
REQUEST_FAILURES = Counter('google_request_failures', 'Number of failed requests to Google')
GOOGLE_STATUS = Gauge('google_up', 'Whether Google is up (1) or down (0)')

@REQUEST_TIME.time()
def fetch_google():
    try:
        response = requests.get("https://www.google.com", timeout=3)
        REQUEST_COUNTER.inc()
        if response.status_code == 200:
            GOOGLE_STATUS.set(1)
        else:
            GOOGLE_STATUS.set(0)
            REQUEST_FAILURES.inc()
    except Exception:
        GOOGLE_STATUS.set(0)
        REQUEST_FAILURES.inc()

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus will scrape here
    while True:
        fetch_google()
        time.sleep(5)