# scripts/test_rag.py

from backend.app.services.retriever import retrieve

from backend.app.services.prompt_builder import (
    build_context,
    build_prompt
)

from backend.app.services.llm import (
    generate_answer
)

query = "What is the leave policy?"

results = retrieve(query)

context = build_context(results)

prompt = build_prompt(
    query,
    context
)

answer = generate_answer(
    prompt
)

print("\nANSWER:\n")
print("\nRETRIEVED CHUNKS:\n")

for chunk in results["documents"][0]:
    print("=" * 50)
    print(chunk[:500])

print("\nANSWER:\n")
print(answer)