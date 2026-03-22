import requests

def ask_ollama(prompt: str, backend_url: str = "http://localhost:11434"):
    """
    Send a prompt to the Ollama backend and return the response.
    """
    try:
        response = requests.post(
            f"{backend_url}/api/generate",
            json={"prompt": prompt}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}