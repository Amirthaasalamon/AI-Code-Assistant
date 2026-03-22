# utils.py
import os
import requests

def ask_ollama(prompt, model="llama3", backend_url=None):
    if backend_url is None:
        backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:11434")
    url = f"{backend_url}/api/generate"
    try:
        response = requests.post(
            url,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("response", "No response")
    except Exception as e:
        return f"❌ Error calling backend: {e}"