import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load .env vars (LangSmith support)
load_dotenv()
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Essay (OpenAI)
def get_openai_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}}
        )
        return response.json()['output']['content']
    except Exception as e:
        return f"❌ Error: {e}"

# Poem (Ollama)
def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}}
        )
        return response.json()['output']['content']
    except Exception as e:
        return f"❌ Error: {e}"

# Streamlit UI
st.title('LangChain Demo with OpenAI & LLAMA2')

input_text = st.text_input("📝 Write an essay on:")
input_text1 = st.text_input("🎵 Write a poem on:")

if input_text:
    st.subheader("Essay Result")
    st.write(get_openai_response(input_text))

if input_text1:
    st.subheader("Poem Result")
    st.write(get_ollama_response(input_text1))
