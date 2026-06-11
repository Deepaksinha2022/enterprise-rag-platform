from backend.app.retrieval.query_expander import (
    expand_query
)

query = "annual leave"

results = expand_query(
    query
)

print(
    results
)