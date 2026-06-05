FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV EXPORT_DIR=/data/generated_projects
ENV STORAGE_DIR=/data/storage
RUN mkdir -p /data/generated_projects /data/storage

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
