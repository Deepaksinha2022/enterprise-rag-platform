from backend.app.retrieval.query_pipeline import (
    process_query
)

queries = process_query(
    "How many vacation days do I get?"
)

print("\nFINAL QUERIES\n")

for q in queries:

    print(q)