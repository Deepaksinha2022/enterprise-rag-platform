# scripts/test_ollama_openai.py

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="llama3.2",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    timeout=300
)

response = llm.invoke(
    "Say hello in one sentence."
)

print(response.content)