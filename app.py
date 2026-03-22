# app.py
import streamlit as st
from utils import ask_ollama
from file_handler import read_uploaded_files
import os

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="AI Code Assistant", layout="wide")

# -------------------------------
# SESSION STATE
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "files_data" not in st.session_state:
    st.session_state.files_data = []

if "theme" not in st.session_state:
    st.session_state.theme = "Ocean"

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    st.title("⚙️ Settings")
    theme = st.radio("🌗 Theme", ["Ocean", "Light"])
    st.session_state.theme = theme

    model = st.selectbox("🤖 Model", ["llama3", "mistral", "gemma"])

    uploaded_files = st.file_uploader(
        "📂 Upload Project Files",
        accept_multiple_files=True
    )

    if uploaded_files:
        st.session_state.files_data = read_uploaded_files(uploaded_files)
        st.success("Files uploaded successfully ✅")

    if st.button("+ New Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# THEMES
# -------------------------------
if st.session_state.theme == "Ocean":
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #0a2540, #133b5c); color: white; }
    section[data-testid="stSidebar"] { background-color: #061a2b; }
    textarea { background: white !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp { background: #f5f7fa; color: black; }
    section[data-testid="stSidebar"] { background-color: #eaeaea; }
    textarea { background: white !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown("""
<h1 style='text-align:center; color:#00d4ff;'>🤖 AI Code Assistant</h1>
<p style='text-align:center; font-size:18px;'>⚡ Logic Over Syntax | Chat + Code AI</p>
""", unsafe_allow_html=True)

# -------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# USER INPUT
# -------------------------------
user_input = st.chat_input("Ask something or paste your code...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # File context
    files_context = ""
    for file in st.session_state.files_data:
        files_context += f"\n\nFile: {file['name']}\n{file['content']}"

    # Smart prompt
    prompt = f"""
You are a professional AI assistant.
Roles:
1. Chat + Code AI
2. Legacy Code Modernization (Java/COBOL → Python)

Instructions:
- Analyze code carefully
- Convert legacy code exactly to Python
- If user asks for output, simulate result correctly
- Always double-check arithmetic or logic

User Input:
{user_input}

Project Files:
{files_context}

Output Format:
1. 👨‍💻 Converted Code
2. 📖 Explanation
3. 🚀 Improvements
4. 💬 Friendly Reply
"""

    # AI RESPONSE
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:11434")
            response = ask_ollama(prompt, model, backend_url=BACKEND_URL)
            st.markdown(response)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response})