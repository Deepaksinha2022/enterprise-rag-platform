# scripts/test_llama3_speed.py

import time

from openai import OpenAI

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

start = time.time()

response = client.chat.completions.create(
    model="llama3",
    temperature=0,
    messages=[
        {
            "role": "user",
            "content":
            "Return JSON: {\"statements\":[\"hello\"]}"
        }
    ]
)

print(
    "Duration:",
    time.time() - start
)

print(
    response.choices[0].message.content
)