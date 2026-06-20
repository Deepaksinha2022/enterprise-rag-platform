import httpx

async def generate_answer(prompt):

    try:
        async with httpx.AsyncClient() as client:

            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=90
            )
        return response.json()["response"]
    except Exception as e:
        return f"LLM Error: {repr(e)}"
    
async def generate_answer_stream(
    prompt
):

    async with httpx.AsyncClient() as client:

        async with client.stream(
            "POST",
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": True
            },
            timeout=90
        ) as response:

            async for line in response.aiter_lines():

                if line:

                    yield line