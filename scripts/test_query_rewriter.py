from backend.app.retrieval.query_rewriter import (
    rewrite_query
)

query = "How many vacation days do I get?"

rewritten = rewrite_query(
    query
)

print(
    "Original:",
    query
)

print(
    "Rewritten:",
    rewritten
)