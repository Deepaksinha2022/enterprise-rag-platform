from backend.app.services.retriever import (
    retrieve
)

results = retrieve(
    "leave policy"
)

print(
    results["documents"][0]
)