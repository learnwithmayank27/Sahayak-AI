from app.engine.router import route_request
from app.db.memory import save_chat, get_chat_history, search_memory, store_memory
from app.agents.agent_manager import AgentManager

agent_manager = AgentManager()
async def generate_ai_response(user_input: str, session_id: str = "default"):

    # Save user input
    save_chat(session_id, f"User: {user_input}")

    # Get history
    history = get_chat_history(session_id)

    # Get semantic memory
    memories = search_memory(user_input)

    # 🤖 RUN AGENTS
    agent_results = await agent_manager.run_agents(user_input)

    response = await route_request(user_input)

    save_chat(session_id, f"AI: {response['response']}")
    store_memory(user_input)

    return {
        "response": response,
        "agents": agent_results,
        "history": history,
        "memories": memories
    }
