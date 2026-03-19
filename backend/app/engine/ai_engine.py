from app.engine.router import route_request

async def generate_ai_response(user_input: str):
    response = await route_request(user_input)
    return response
