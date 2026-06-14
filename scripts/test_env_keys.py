import os

from dotenv import load_dotenv

load_dotenv()

print(
    "LANGSMITH_API_KEY =",
    bool(os.getenv("LANGSMITH_API_KEY"))
)

print(
    "LANGCHAIN_API_KEY =",
    bool(os.getenv("LANGCHAIN_API_KEY"))
)

print(
    "LANGSMITH_PROJECT =",
    os.getenv("LANGSMITH_PROJECT")
)

print(
    "LANGCHAIN_PROJECT =",
    os.getenv("LANGCHAIN_PROJECT")
)