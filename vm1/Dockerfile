FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Inicia FastAPI e mantém o container ativo
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & tail -f /dev/null"]

