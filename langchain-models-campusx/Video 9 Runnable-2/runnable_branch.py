from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Create a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Create a summary on {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

detailed_report_runnable = RunnableSequence(prompt1, model, parser)

runnable_branch = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(detailed_report_runnable, runnable_branch)

result = final_chain.invoke({'topic': 'ABESEC is the worst college'})

print(result)