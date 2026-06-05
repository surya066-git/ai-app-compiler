# Frontend build stage
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# Backend production stage
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uvicorn gunicorn

# Copy backend code
COPY backend/ ./backend/

# Copy frontend build output to serve as static files if needed, 
# or keep them separate depending on deployment strategy.
# For simplicity, we assume separate deployment or nginx routing.
# But we copy it just in case backend serves it.
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

EXPOSE 8000

WORKDIR /app/backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
