from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ollama  # official Python client

app = FastAPI(title="AI Code Assistant Backend")

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class AIRequest(BaseModel):
    prompt: str
    model: str

@app.post("/api/generate")
def generate(req: AIRequest):
    try:
        # Call Ollama's Python generate
        result = ollama.generate(model=req.model, prompt=req.prompt)
        return {"response": result.get("response", "")}
    except Exception as e:
        return {"response": f"❌ Error calling Ollama: {e}"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=11434)