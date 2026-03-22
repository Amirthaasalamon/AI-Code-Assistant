# AI-Code-Assistant
 AI Code Assistant – Legacy Code Modernization Chatbot  

 
An intelligent AI-powered chatbot that helps developers convert, understand, and modernize legacy code using local LLMs via Ollama.

 Overview

The AI Code Assistant is a hybrid chatbot that combines:

💬 Conversational AI

💻 Legacy Code Conversion

📖 Code Explanation

It can transform outdated code (Java/COBOL) into modern Python while maintaining logic and improving readability.

🚀 Features

💬 Chatbot Interface – Friendly, ChatGPT-like experience

💻 Legacy Code Conversion – Java/COBOL → Python

📖 Code Explanation – Step-by-step understanding

📂 File Upload Support – Analyze multiple project files

🤖 Multi-Model Support – llama3, mistral, gemma

🎨 Custom UI Themes – Ocean & Light mode

🔄 Chat History – Session-based memory

⚡ Local AI Execution – No API cost (runs via Ollama)

🖥️ Demo

Input (Legacy Java)

public int add(int a, int b){
    return a + b;
}
Output (Python)

def add(a, b):
    return a + b
    
🏗️ Project Structure

project/
|

│__chatbot.py

|__cleaner.py

├── app.py       # Streamlit UI

├── utils.py # Ollama API connection

├── file_handler.py     # File upload handling

├── requirements.txt

└── README.md

⚙️ Installation

1️⃣ Install Ollama

Download: https://ollama.com

Pull a model:

ollama pull llama3

2️⃣ Clone Repository

git clone https://github.com/Amirthaasalamon/ai-code-assistant.git
cd ai-code-assistant

3️⃣ Install Dependencies

python -m pip install -r requirements.txt

4️⃣ Run the App

python -m streamlit run app.py

🧠 How It Works

User inputs query or legacy code

Optional files are uploaded for context

A smart prompt is generated

Prompt is sent to Ollama

AI returns:

Converted code

Explanation

Improvements

🛠️ Tech Stack

Python

Streamlit

Ollama

LLMs: LLaMA3, Mistral, Gemma

Requests (API calls)

⚠️ Challenges Solved

Handling legacy code complexity

Reducing AI hallucinations

Managing multi-file context


Creating a smooth developer experience

💡 Use Cases

Legacy system modernization

Learning new programming languages

Code debugging and explanation

Developer productivity tool

🚀 Future Enhancements

🔹 GitHub repository integration

🔹 Multi-file dependency graph

🔹 Database for chat history

🔹 Authentication system

🔹 Cloud deployment (AWS / Render)

🤝 Contributing

Contributions are welcome!

Feel free to fork this repo and submit a pull request.

📄 License

This project is licensed under the MIT License.

⭐ Support

If you like this project, give it a ⭐ on GitHub
