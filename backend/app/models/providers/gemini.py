import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_gemini_response(prompt: str, model_name="models/gemini-2.5-flash"):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini error: {str(e)}"
