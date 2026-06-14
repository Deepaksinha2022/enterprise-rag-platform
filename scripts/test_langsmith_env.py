import os

from dotenv import load_dotenv

load_dotenv()

print(
    os.getenv(
        "LANGCHAIN_PROJECT"
    )
)

print(
    os.getenv(
        "LANGCHAIN_TRACING_V2"
    )
)