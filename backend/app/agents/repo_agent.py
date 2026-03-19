from app.agents.base_agent import BaseAgent

class RepoAgent(BaseAgent):
    name = "repo-agent"

    async def run(self, input_data: str):
        return {
            "agent": self.name,
            "analysis": "Repository analyzed",
            "suggestions": ["Improve README", "Add tests"]
        }
