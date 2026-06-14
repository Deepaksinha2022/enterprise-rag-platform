from dotenv import load_dotenv
load_dotenv()

from langsmith import Client

client = Client()

print(
    "Client created successfully"
)

print(
    "Projects:",
    client.list_projects(limit=5)
)