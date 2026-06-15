# scripts/test_instructor_ollama.py

from openai import OpenAI
from ragas.llms import llm_factory

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

llm = llm_factory(
    model="llama3.2",
    provider="openai",
    client=client
)

print(type(llm))
print(llm)