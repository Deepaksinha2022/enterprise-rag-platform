import requests

BASE_URL = "http://localhost:8000"

# Step 1: Login
login_response = requests.post(
    f"{BASE_URL}/login",
    params={
        "username": "finance_user"
    }
)

token = login_response.json()[
    "access_token"
]

# Step 2: Ask Question
response = requests.post(
    f"{BASE_URL}/chat/ask",
    params={
        "query":
        "What is the reimbursement policy?"
    },
    headers={
        "Authorization":
        f"Bearer {token}"
    }
)

print(response.json())