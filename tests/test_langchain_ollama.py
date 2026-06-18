from langchain_ollama import ChatOllama

print("Creating model...")

llm = ChatOllama(
    model="llama3.2:3b"
)

response = llm.invoke(
    "What is prompt injection?"
)

print("\nResponse:\n")
print(response.content)