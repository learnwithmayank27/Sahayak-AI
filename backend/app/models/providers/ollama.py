import httpx

OLLAMA_URL = "http://172.17.0.1:11434/api/generate"

async def generate_ollama_response(prompt: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=600
            )
            return response.json()["response"]
    except Exception as e:
        return f"Ollama error: {str(e)}"
