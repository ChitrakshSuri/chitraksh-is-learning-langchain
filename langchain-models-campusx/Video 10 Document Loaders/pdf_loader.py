from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample.pdf')

docs = loader.load()

print(len(docs))
print(docs[1].page_content)