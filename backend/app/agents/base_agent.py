class BaseAgent:
    name = "base"

    async def run(self, input_data: str):
        raise NotImplementedError("Agent must implement run()")
