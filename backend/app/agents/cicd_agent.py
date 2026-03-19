from app.agents.base_agent import BaseAgent

class CICDAgent(BaseAgent):
    name = "cicd-agent"

    async def run(self, input_data: str):
        return {
            "agent": self.name,
            "analysis": "CI/CD pipeline failure detected",
            "solution": "Check logs and retry pipeline"
        }
