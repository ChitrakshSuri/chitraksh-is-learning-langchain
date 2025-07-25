from langchain_huggingface import HuggingFaceEmbeddings
import os
os.environ["TRANSFORMERS_CACHE"] = r"E:\CODE\AI Agents\hf_cache"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India."

vector = embedding.embed_query(text)
print(str(vector))