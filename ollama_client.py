import requests

def ask_ollama(prompt, model="deepseek-coder"):
    url = "http://localhost:11434/api/generate"

    response = requests.post(url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]