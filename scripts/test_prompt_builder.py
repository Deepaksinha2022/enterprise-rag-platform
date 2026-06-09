from backend.app.services.retriever import (
    retrieve
)

from backend.app.services.prompt_builder import (
    build_context,
    build_prompt
)


query = "leave policy"

results = retrieve(
    query
)

context = build_context(
    results
)

prompt = build_prompt(
    query,
    context
)

print(prompt)