from backend.app.services.embeddings import (
    generate_embeddings
)

from sklearn.metrics.pairwise import cosine_similarity

texts = [

    "Employee annual leave policy",

    "Staff vacation rules",

    "How to bake a chocolate cake"

]

embeddings = generate_embeddings(
    texts
)

sim_1 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

sim_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)

print()
print(sim_1,type(sim_1))
print(sim_2,type(sim_2))
print(
    "Leave vs Vacation:",
    sim_1[0][0]
)

print()

print(
    "Leave vs Cake:",
    sim_2[0][0]
)