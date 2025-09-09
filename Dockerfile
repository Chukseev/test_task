FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r requirements.txt
COPY . .
ENV PATH="/opt/venv/bin:$PATH"
CMD bash -c "until pg_isready -h db -p 5432 -U postgres; do echo 'Waiting for Postgres...'; sleep 2; done && \
            python manage.py migrate --noinput && \
            python manage.py runserver 0.0.0.0:8000"
