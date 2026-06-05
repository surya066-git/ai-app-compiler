def generate_docker_setup() -> dict:
    """
    Generates deployment-ready Dockerfile, docker-compose.yml and .env.example
    Returns a dictionary mapping filepaths to file contents.
    """
    dockerfile_content = """# Frontend build stage
FROM node:20-alpine AS frontend-builder
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
"""

    docker_compose_content = """version: '3.8'

services:
  backend:
    build: 
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql+psycopg://user:password@db:5432/appdb
      - JWT_SECRET_KEY=change_me_in_production
    depends_on:
      - db
      
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=appdb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""
    
    env_example_content = """DATABASE_URL=postgresql+psycopg://user:password@db:5432/appdb
JWT_SECRET_KEY=change_me_in_production
VITE_API_URL=http://localhost:8000
"""

    return {
        "Dockerfile": dockerfile_content,
        "docker-compose.yml": docker_compose_content,
        ".env.example": env_example_content
    }
