from backend.app.services.llm import (
    generate_answer
)

answer = generate_answer(
    "What is AI in one sentence?"
)

print(answer)