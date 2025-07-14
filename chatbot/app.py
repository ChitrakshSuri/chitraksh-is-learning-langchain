from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# env vars
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the user's queries."),
    ("user", "Question: {question}")
])

# streamlit UI
st.title("LangChain Demo With OpenAI API")
input_text = st.text_input("Search the topic you want")

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    result = chain.invoke({"question": input_text})
    st.write(result)
