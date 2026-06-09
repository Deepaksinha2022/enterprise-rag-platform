from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

texts = [

    "Employee annual leave policy",

    "Staff vacation rules",

    "How to bake a chocolate cake"

]


models = {

    "MiniLM":
    "sentence-transformers/all-MiniLM-L6-v2",

    "BGE":
    "BAAI/bge-small-en-v1.5"

}


for model_name, model_path in models.items():

    print()

    print("=" * 50)

    print(model_name)

    print("=" * 50)

    model = SentenceTransformer(
        model_path
    )

    embeddings = model.encode(
        texts
    )

    sim_1 = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    sim_2 = cosine_similarity(
        [embeddings[0]],
        [embeddings[2]]
    )[0][0]

    print(
        "Leave vs Vacation:",
        sim_1
    )

    print(
        "Leave vs Cake:",
        sim_2
    )

    print(
        "Embedding Dimension:",
        len(embeddings[0])
    )