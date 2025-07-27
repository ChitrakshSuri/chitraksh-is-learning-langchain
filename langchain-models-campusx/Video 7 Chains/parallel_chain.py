from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

load_dotenv()

# Initialize two different OpenAI models
model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = ChatOpenAI(model="gpt-4")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chian = prompt3 | model1 | parser

chain = parallel_chain | merge_chian

text = """
Support Vector Machines (SVMs) are powerful supervised learning models used for classification, regression, and outlier detection.

Key characteristics of SVMs include:

- They work by finding the optimal hyperplane that separates data points of different classes.
- SVMs are effective in high-dimensional feature spaces.
- They use a subset of training points called support vectors, making them memory efficient.
- The kernel trick allows SVMs to model non-linear decision boundaries.
- SVMs are robust to overfitting, especially in high-dimensional settings.

Common kernels used in SVMs are:
- Linear
- Polynomial
- Radial Basis Function (RBF)
- Sigmoid
"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()