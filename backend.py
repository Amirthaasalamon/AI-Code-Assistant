# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn
import os

app = FastAPI()

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: bool = False

# Replace this with your Ollama server URL if needed
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")

@app.post("/api/generate")
def generate(req: GenerateRequest):
    url = f"{OLLAMA_URL}/api/generate"
    payload = {
        "model": req.model,
        "prompt": req.prompt,
        "stream": req.stream
    }
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        return {"response": response.json().get("response", "No response")}
    except Exception as e:
        return {"response": f"❌ Error calling Ollama backend: {e}"}

if __name__ == "__main__":
    # Use environment variable PORT for deployment platforms
    port = int(os.getenv("PORT", 11434))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")