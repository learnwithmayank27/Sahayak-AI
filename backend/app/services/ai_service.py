from app.engine.ai_engine import generate_ai_response

async def process_chat(user_input: str):
    response = await generate_ai_response(user_input)
    return response
