from sentence_transformers import SentenceTransformer


def generate_embeddings(texts):
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    embeddings = model.encode(texts)

    return embeddings