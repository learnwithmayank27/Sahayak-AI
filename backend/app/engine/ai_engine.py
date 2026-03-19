from app.engine.router import route_request
from app.db.memory import save_chat, get_chat_history, search_memory, store_memory

async def generate_ai_response(user_input: str, session_id: str = "default"):

    # Save user input
    save_chat(session_id, f"User: {user_input}")

    # Get history
    history = get_chat_history(session_id)

    # Get semantic memory
    memories = search_memory(user_input)

    # Route request
    response = await route_request(user_input)

    # Save AI response
    save_chat(session_id, f"AI: {response['response']}")

    # Store long-term memory
    store_memory(user_input)

    return {
        "response": response,
        "history": history,
        "memories": memories
    }
