from backend.app.retrieval.reranker import (
    rerank
)

docs = [

    "Annual Leave Policy",

    "Sick Leave Policy",

    "Attendance Policy"
]

results = rerank(
    "sick leave policy",
    docs
)

for doc, score in results:

    print(
        score,
        doc
    )