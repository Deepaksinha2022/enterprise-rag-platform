import pandas as pd

from backend.app.services.embeddings import generate_embeddings

from backend.app.services.vector_store import search_chunks

df = pd.read_csv("retrieval_evaluation_dataset.csv")

k = 10

total_precision = 0
total_recall = 0
total_hits = 0

for _, row in df.iterrows():

    question = row["question"]
    
    expected_chunk_id = str(row["expected_chunk_id"])

    query_embedding = generate_embeddings([question])[0]

    results = search_chunks(
        query_embedding=query_embedding,
        k=k
    )

    retrieved_ids = results["ids"][0]

    if expected_chunk_id not in retrieved_ids:

        print("\nFAILED")
        print("Question:", question)
        print("Expected:", expected_chunk_id)
        print("Retrieved:", retrieved_ids)

    relevant_found = 1 if expected_chunk_id in retrieved_ids else 0

    precision = relevant_found / k
    recall = relevant_found / 1

    total_precision += precision
    total_recall += recall
    total_hits += relevant_found

precision_at_k = total_precision / len(df)
recall_at_k = total_recall / len(df)
hit_rate = total_hits / len(df)

print(f"Precision@{k}: {precision_at_k:.4f}")
print(f"Recall@{k}: {recall_at_k:.4f}")
print(f"HitRate@{k}: {hit_rate:.4f}")