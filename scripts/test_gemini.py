import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = """
Return ONLY valid JSON.

Schema:

{
  "statements": [
    "statement 1",
    "statement 2"
  ]
}

Text:
The reimbursement policy allows employees to claim legitimate business expenses.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)