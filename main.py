from fastapi import FastAPI
app = FastAPI(title="API Centelha com guardrails")
@app.get("/")
def home():
    return {"mensagem": "Sistema de regulação online"}
