from app.models.model_manager import ModelManager

model_manager = ModelManager()

async def route_request(user_input: str):

    user_input_lower = user_input.lower()

    if "code" in user_input_lower:
        model_type = "ollama"

    elif "explain" in user_input_lower:
        model_type = "gemini"

    else:
        model_type = "auto"

    response = await model_manager.generate(user_input, model_type)

    return {
        "model": model_type,
        "response": response
    }
