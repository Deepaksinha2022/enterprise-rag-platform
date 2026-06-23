from groq import AsyncGroq
import os

client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY")
)

async def generate_answer(prompt):

    try:

        response = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"LLM Error: {repr(e)}"
    
async def generate_answer_stream(prompt):

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        stream=True
    )

    async for chunk in response:

        content = (
            chunk.choices[0]
            .delta
            .content
        )

        if content:

            yield content