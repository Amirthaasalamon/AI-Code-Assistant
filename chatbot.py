from ollama_client import ask_ollama
from cleaner import clean_code, optimize_context

def convert_code(code):
    try:
        # Clean the code
        cleaned = clean_code(code)

        # Optimize context (limit size)
        context = optimize_context(cleaned)

        # Prompt for AI
        prompt = f"""
You are a senior software engineer.

Convert the following code into modern Python.

Rules:
- Keep logic EXACT
- Do NOT hallucinate
- If unclear, say UNKNOWN

Code:
{context}

Output:
- Python code
- Explanation
"""

        # Call Ollama
        response = ask_ollama(prompt)

        return response

    except Exception as e:
        return f"Error: {e}"