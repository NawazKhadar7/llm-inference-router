FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "scripts/serve.py", "--port", "8080"]
