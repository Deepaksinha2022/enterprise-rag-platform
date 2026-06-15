import pandas as pd

from backend.app.services.hybrid_service import (
    hybrid_retrieve
)

from backend.app.services.prompt_builder import (
    build_context,
    build_prompt
)

from backend.app.services.llm import (
    generate_answer
)

df = pd.read_csv(
    "evaluation_dataset.csv"
)

rows=[]


for _, row in df.iterrows():

   

    question = row["question"]

    results = hybrid_retrieve(
        question
    )

    context = build_context(
        results
    )

    prompt = build_prompt(
        question,
        context
    )

    answer = generate_answer(
        prompt
    )

    rows.append(
    {
        "question": question,
        "ground_truth": row["ground_truth"],
        "generated_answer": answer,
        "retrieved_context": context
    }
)
    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer[:300])

    print("\n" + "=" * 50)

results_df = pd.DataFrame(
    rows
)

results_df.to_csv(
    "evaluation_results.csv",
    index=False
)

print(
    "evaluation_results.csv created"
)