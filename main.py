from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

# Para gerar o token, use:
# openssl rand -hex 32 
API_TOKEN = "05dec1c71e3fdfc32e951e221c479b0f45c6304bb191394837f6502de25763e5"

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API Aviator no ar com sucesso 🚀"}

@app.post("/prever")
async def prever(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")

    token = auth.split(" ")[1]
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Token inválido")

    # Aqui entra a lógica com seu modelo `.pkl`
    # Exemplo de resposta simulada:
    return {"previsao": "valor fictício", "status": "OK"}
