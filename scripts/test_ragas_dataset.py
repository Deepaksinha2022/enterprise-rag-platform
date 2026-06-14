from datasets import Dataset

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

print(dataset)