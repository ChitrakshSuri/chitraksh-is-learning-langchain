# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text:\n{topic}',
    input_variables=['topic']
)

# Generate detailed report
prompt1 = template1.invoke({'topic': 'black hole'})
result = model.invoke(prompt1)

# Generate summary
prompt2 = template2.invoke({'topic': result.content})
result1 = model.invoke(prompt2)

print(result1.content)
