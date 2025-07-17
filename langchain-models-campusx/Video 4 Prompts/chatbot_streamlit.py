import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from datetime import datetime

# Load .env
load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="🧠 AI Research Chat Assistant", page_icon="🤖", layout="centered")

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")

# Model selection
selected_model = st.sidebar.selectbox("Choose Model", ["gpt-3.5-turbo", "gpt-4"])

# Theme mode info
st.sidebar.markdown("🌓 **Theme mode** follows your browser or Streamlit settings.")
st.sidebar.markdown("To change manually:\n\n```bash\nstreamlit settings set theme.base \"dark\"\n```")

# Clear chat button
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []

# Export chat history
if st.sidebar.button("💾 Export as Markdown"):
    if "chat_history" in st.session_state and st.session_state.chat_history:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_history_{timestamp}.md"
        chat_md = "\n\n".join(
            [f"**User:** {m.content}" if isinstance(m, HumanMessage) else f"**AI:** {m.content}"
             for m in st.session_state.chat_history]
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(chat_md)
        st.sidebar.success(f"Saved as {filename}")
    else:
        st.sidebar.warning("No chat history to export.")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🧠 AI Research Chat Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Chat with an AI about papers, topics, and tech!</p>", unsafe_allow_html=True)

# --- Initialize Model ---
model = ChatOpenAI(model=selected_model)

# --- Chat History State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Display Chat ---
for msg in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# --- Chat Input ---
user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant"):
        response = model.invoke(st.session_state.chat_history)
        st.markdown(response.content)
        st.session_state.chat_history.append(AIMessage(content=response.content))
