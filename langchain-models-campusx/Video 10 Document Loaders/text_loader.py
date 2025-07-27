from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='write a summary in {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

loader = TextLoader('sample_doc.txt', encoding='utf-8')

docs = loader.load()

print(docs)
print(type(docs))
print(docs[0])
print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'topic': docs[0].page_content})

print(result)