from openai import OpenAI

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = client.chat.completions.create(
    model="llama3",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a JSON API. "
                "Return ONLY valid JSON. "
                "Do not explain anything. "
                "Do not use markdown."
            )
        },
        {
            "role": "user",
            "content": """
Return ONLY this JSON schema:

{
  "statements": [
    "string"
  ]
}

Do not create any other keys.

Question:
What is the reimbursement policy?

Answer:
The university's expense reimbursement policy allows reimbursement of legitimate work-related expenses.
"""
        }
    ]
)

print(response.choices[0].message.content)