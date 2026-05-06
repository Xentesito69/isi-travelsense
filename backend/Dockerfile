# ── Stage 1: build ──────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies in a separate layer for caching
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Stage 2: runtime ─────────────────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Install curl (needed for Docker healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy application source
COPY . .

# Entrypoint: initializa la BD si no existe y arranca gunicorn
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# SQLite DB lives in a mounted volume so data survives pod restarts
VOLUME ["/app/data"]

# Point the app at the volume path for the DB
ENV DB_PATH=/app/data/travelsense.db

EXPOSE 5000

# Use gunicorn for production (more robust than Flask dev server)
RUN pip install --no-cache-dir gunicorn

ENTRYPOINT ["/entrypoint.sh"]
