import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaW5hbmNlX3VzZXIifQ.ZDfi-Yrb_sQH-f91HDh6KA_Ho40my5cupY-WLGe0Byc"

with open(
    "benchmark_queries.txt",
    "r"
) as file:

    queries = [
        q.strip()
        for q in file.readlines()
        if q.strip()
        and not q.startswith("#")
    ]

for query in queries:

    print(
        f"Running: {query}"
    )

    requests.post(
        "http://127.0.0.1:8000/chat/ask",
        params={
            "query": query
        },
        headers={
            "Authorization":
            f"Bearer {TOKEN}"
        }
    )