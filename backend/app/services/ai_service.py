from app.engine.ai_engine import generate_ai_response

async def process_chat(user_input: str, session_id: str):
    return await generate_ai_response(user_input, session_id)
