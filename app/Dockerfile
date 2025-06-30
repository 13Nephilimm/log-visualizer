FROM python:3.10

WORKDIR /app

COPY app.py .

RUN pip install requests prometheus_client

CMD ["python", "app.py"]