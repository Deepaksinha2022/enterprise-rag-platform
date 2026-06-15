import requests

BASE_URL = "http://localhost:8000"

response = requests.post(
    f"{BASE_URL}/login",
    params={
        "username": "finance_user"
    }
)

print(response.json())