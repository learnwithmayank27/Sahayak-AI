from app.agents.base_agent import BaseAgent

class LogAgent(BaseAgent):
    name = "log-agent"

    async def run(self, input_data: str):
        if "error" in input_data.lower():
            return {
                "agent": self.name,
                "analysis": "Error found in logs",
                "solution": "Check stack trace"
            }
        return {"agent": self.name, "analysis": "No major issue"}
