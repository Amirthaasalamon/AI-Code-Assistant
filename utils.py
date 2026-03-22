import os
import requests

def ask_ollama(prompt, model="llama3", backend_url=None):
    """
    Calls the backend AI server and returns the response.
    """
    if backend_url is None:
        backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:11434")
    
    url = f"{backend_url}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}

    try:
        response = requests.post(url, json=payload, timeout=120)  
        response.raise_for_status()
        return response.json().get("response", "No response from backend")
    except Exception as e:
        return f"❌ Error calling backend: {e}"