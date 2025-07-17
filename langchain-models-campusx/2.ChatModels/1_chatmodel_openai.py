from langchain_openai import ChatOpenAI  # using chat model not llm
from dotenv import load_dotenv

load_dotenv()

# temprature means the chat model will give creative or deterministic ans - 39:00 video 3 campusX
# tokens can be roughly considered as words
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)


result = model.invoke("Write 5 line poem on Pig.")
# print(result)
print(result.content)
