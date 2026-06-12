from backend.app.services.retriever import (
    retrieve
)

results = retrieve(
    "leave policy",
    department="HR"
)

print(
    results["metadatas"][0][0]["department"]
)