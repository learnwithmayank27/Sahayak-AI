async def route_request(user_input: str):
    user_input_lower = user_input.lower()

    if "code" in user_input_lower:
        return {"model": "deepseek", "response": "Code-related response"}
    
    elif "error" in user_input_lower:
        return {"model": "debug-agent", "response": "Debugging response"}
    
    else:
        return {"model": "gemini", "response": "General response"}
