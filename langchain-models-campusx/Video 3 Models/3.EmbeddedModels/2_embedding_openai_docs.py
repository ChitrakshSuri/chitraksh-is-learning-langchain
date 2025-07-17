from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "The capital of France is Paris.",
    "Tokyo is the capital of Japan.",
    "Canberra is the capital of Australia.",
]

result = embedding.embed_documents(documents)
print(str(result))
