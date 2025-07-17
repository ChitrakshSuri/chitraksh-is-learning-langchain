from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# langchian is not mature frame work so this is how we should use SystemMessage, and HumanMessage for dynamic input
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})
print(prompt)
