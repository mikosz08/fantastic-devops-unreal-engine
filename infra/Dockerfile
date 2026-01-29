FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY tools /app/tools
WORKDIR /app/tools

RUN pip install flask prometheus_client

CMD ["python", "run_metrics.py"]
