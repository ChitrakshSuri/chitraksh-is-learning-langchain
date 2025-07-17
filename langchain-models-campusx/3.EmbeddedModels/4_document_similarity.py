from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

doccuments = [
    "Virat Kohli is a famous cricketer known for his aggressive batting style.",
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",
    "Lionel Messi is a world-renowned football player with numerous awards.",
    "Cristiano Ronaldo is a legendary footballer known for his goal-scoring ability.",
    "Rohit Sharma is the captain of the Indian cricket team and a prolific run-scorer.",
    "Kylian Mbappe is a young football star known for his speed and skill.",
]

query = "tell me about bumrah"

doccument_embeddings = embedding.embed_documents(doccuments)
query_embedding = embedding.embed_query(query)

# print(cosine_similarity([query_embedding], doccument_embeddings))
scores = cosine_similarity([query_embedding], doccument_embeddings)
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(query)
print(doccuments[index])
print("similarity score is: ", score)
