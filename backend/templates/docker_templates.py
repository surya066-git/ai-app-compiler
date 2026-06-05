DOCKERFILE_BACKEND = """
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

DOCKERFILE_FRONTEND = """
FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev", "--", "--host"]
"""

DOCKER_COMPOSE = """
version: '3.8'

services:
  backend:
    build: 
      context: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql+psycopg://user:password@db:5432/{db_name}
      - JWT_SECRET_KEY={jwt_secret}
    depends_on:
      - db

  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://localhost:8000
    depends_on:
      - backend

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB={db_name}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""
