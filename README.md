# Google.com Log Visualizer

This is a small monitoring app that checks `google.com` response status and time, and visualizes it using Prometheus and Grafana.

## 🔧 Requirements

- Docker + Docker Compose

## 🚀 How to Run

1. Clone the repo:
   git clone https://github.com/13Nephilimm/log-visualizer.git
   cd log-visualizer

2. Run the app
   docker-compose up --build

3. Open in browser
   Python metrics: http://localhost:8000
   Prometheus: http://localhost:9090
   Grafana: http://localhost:3000

   Grafana default login: admin / admin

## ✨ Visualizes:

- google_up – Google availability (1 = up, 0 = down)

- google_request_duration_seconds – Response time

- google_request_count – Total requests

- google_request_failures – Failed requests

## 📦 Services

Service Port
Python App 8000
Prometheus 9090
Grafana 3000
