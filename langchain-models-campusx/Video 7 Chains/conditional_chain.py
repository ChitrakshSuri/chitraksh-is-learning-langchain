from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

# Define pydantic schema for sentiment classification


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description='Give the sentiment of the feedback'
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt to classify sentiment
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n{feedback} \n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

# Prompts for positive/negative responses
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n{feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n{feedback}',
    input_variables=['feedback']
)

# String parser for final response
parser = StrOutputParser()

# Conditional chain based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

classifier_chian = prompt1 | model | parser2

chain = classifier_chian | branch_chain

# Run the chain
result = chain.invoke({'feedback': 'this is a terrible smartphone'})

print(result)
