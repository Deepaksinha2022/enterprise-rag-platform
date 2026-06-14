# scripts/test_ragas_ollama.py

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness

from langchain_openai import ChatOpenAI

import time

evaluator_llm = ChatOpenAI(
    model="llama3.2",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    timeout=300,
    max_retries=1
)

data = {
    "question": [
        "What is the reimbursement policy?"
    ],
    "answer": [
        "The expense reimbursement policy outlines reimbursement for university expenses incurred by faculty and staff."
    ],
    "contexts": [[
        "The expense reimbursement policy outlines reimbursement for university expenses incurred by faculty and staff."
    ]],
    "ground_truth": [
        "The expense reimbursement policy outlines reimbursement for university expenses incurred by faculty and staff."
    ]
}

dataset = Dataset.from_dict(data)


start = time.time()

result = evaluate(
    dataset,
    metrics=[faithfulness],
    llm=evaluator_llm
)

print(
    "Duration:",
    round(time.time() - start, 2),
    "seconds"
)

print(result)
