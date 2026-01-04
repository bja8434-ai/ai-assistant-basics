from fastapi import FastAPI
from app.schemas import ChatRequest
from services.chat_service import build_reply

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Hello from FastAPI (RAG stub mode)"
    }

@app.post("/chat")
def chat(req: ChatRequest):
    query = req.message.strip()
    if not query:
        return {
            "reply": "Type something and I’ll search the docs.",
            "sources": []
        }
    return build_reply(query)
