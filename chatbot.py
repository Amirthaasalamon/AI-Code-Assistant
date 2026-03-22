from ollama_client import ask_ollama
from cleaner import clean_code, optimize_context

def convert_code(user_input, model="deepseek-coder", files_context=""):
    try:
        cleaned = clean_code(user_input)
        context = optimize_context(cleaned)

        prompt = f"""
You are an intelligent, friendly, and professional AI assistant.

Your roles:
1. General Chat Assistant
2. Legacy Code Modernization Expert

Behavior:
- Greet user if message is simple (hi, hello)
- If normal chat → respond naturally
- If code → convert to Python + explain
- Do NOT hallucinate
- If unsure → say UNKNOWN

User Input:
{context}

Project Files:
{files_context}

Output:
1. Converted Code (if any)
2. Explanation
3. Improvements
4. Friendly reply
"""

        response = ask_ollama(prompt, model)

        return response

    except Exception as e:
        return f"Error: {e}"