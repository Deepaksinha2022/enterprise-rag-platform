import pandas as pd
import requests

BASE_URL = "http://localhost:8000"

# Login
login_response = requests.post(
    f"{BASE_URL}/login",
    params={
        "username": "finance_user"
    }
)

token = login_response.json()[
    "access_token"
]

# Load questions
df = pd.read_csv(
    "tests/regression_questions.csv"
)

results = []

for _, row in df.iterrows():

    question = row["question"]
    keyword = row["expected_keyword"]

    response = requests.post(
        f"{BASE_URL}/chat/ask",
        params={
            "query": question
        },
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    answer = response.json()[
        "answer"
    ]

    passed = (
        keyword.lower()
        in answer.lower()
    )

    results.append(
        {
            "question": question,
            "expected_keyword": keyword,
            "passed": passed
        }
    )

result_df = pd.DataFrame(
    results
)

print(result_df)

result_df.to_csv(
    "tests/regression_results.csv",
    index=False
)

total_tests = len(result_df)

passed_tests = result_df[
    "passed"
].sum()

pass_rate = (
    passed_tests
    / total_tests
) * 100

print(
    f"\nPass Rate: "
    f"{pass_rate:.2f}%"
)


print(
    "\nResults saved to tests/regression_results.csv"
)