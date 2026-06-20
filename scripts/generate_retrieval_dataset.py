from backend.app.services.vector_store import collection

from backend.app.services.llm import generate_answer

import asyncio

results = collection.get(
    include=["documents", "metadatas"]
)

questions = []

import pandas as pd

rows = []

for i, (doc, meta) in enumerate(
    zip(results["documents"], results["metadatas"])
):

    if i >= 20:
        break

    print("\n" + "=" * 80)

    print("CHUNK_ID:", meta["chunk_id"])
    
    questions.append({
    "chunk_id": meta["chunk_id"],
    "text": doc[:1500]
    })

    print(f"Added chunk {meta['chunk_id']}")

    prompt = f"""
    
    Generate 2 retrieval-friendly questions.

    Rules:
    - Use exact terminology from the text.
    - Do not paraphrase heavily.
    - Questions must be answerable from the text alone.
    - Focus on definitions, policies, responsibilities, requirements and procedures.
    - Return only questions.

    Text:
    {doc[:1500]}
    """

    response = asyncio.run(
    generate_answer(prompt)
    )

    questions = response.split("\n")[:2]

    for question in questions:

        question = question.strip()

        if not question:
            continue

        rows.append({
            "question": question,
            "expected_chunk_id": meta["chunk_id"]
        })

print("Rows to save:", len(rows))

df = pd.DataFrame(rows)

df.to_csv(
    "retrieval_evaluation_dataset.csv",
    index=False
)

print(
    f"Saved {len(df)} questions"
)
