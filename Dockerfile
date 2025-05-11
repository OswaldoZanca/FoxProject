# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Dependencias del sistema
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev netcat-openbsd \
  && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY scripts/entrypoint.sh /entrypoint.sh
COPY scripts/wait_for_db.sh /wait_for_db.sh
RUN chmod +x /entrypoint.sh /wait_for_db.sh

ENTRYPOINT ["/entrypoint.sh"]
