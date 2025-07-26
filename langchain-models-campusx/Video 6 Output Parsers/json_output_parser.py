from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# ✅ Correct way: Initialize HuggingFaceEndpoint first
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# ✅ Pass llm to ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# ✅ Create parser instance (not class directly)
parser = JsonOutputParser()

# ✅ Use parser's method for format instructions
template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# ✅ Format the prompt
prompt = template.format()

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)
print(type(final_result))

# If you want to run the prompt and parse:
# response = model.invoke(prompt)
# print(parser.parse(response.content))
