from app.models.providers.gemini import generate_gemini_response
from app.models.providers.ollama import generate_ollama_response

class ModelManager:

    async def generate(self, prompt: str, model_type: str = "auto"):

        prompt_lower = prompt.lower()

        try:
            # 🧠 HEAVY TASKS → PRO MODEL
            if any(x in prompt_lower for x in ["debug", "architecture", "design", "analyze"]):
                return await generate_gemini_response(prompt, "models/gemini-2.5-pro")

            # ⚡ DEFAULT → FLASH
            elif model_type == "gemini" or model_type == "auto":
                return await generate_gemini_response(prompt, "models/gemini-2.5-flash")

            # 🧠 LOCAL → OLLAMA
            elif model_type == "ollama":
                return await generate_ollama_response(prompt)

        except Exception:
            # 🔥 FALLBACK SYSTEM
            return await generate_ollama_response(prompt)
