FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Exponha a porta em que a aplicação FastAPI será executada
EXPOSE 3000 # Verifique se sua aplicação FastAPI realmente escuta na porta 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
