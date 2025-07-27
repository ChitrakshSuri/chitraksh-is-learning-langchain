from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Create a linkedin post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Create a X post on {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'linkedin': RunnableSequence(prompt1, model, parser),
    'twitter': RunnableSequence(prompt2, model, parser),
})

result = parallel_chain.invoke({'topic': 'AI'})
print(result)
print(result['twitter'])
