from datasets import Dataset

from ragas import evaluate
from ragas.metrics import faithfulness

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

dataset = Dataset.from_dict(
    data
)

result = evaluate(
    dataset,
    metrics=[
        faithfulness
    ]
)

print(result)