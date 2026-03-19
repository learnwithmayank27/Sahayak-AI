from app.agents.k8s_agent import KubernetesAgent
from app.agents.cicd_agent import CICDAgent
from app.agents.log_agent import LogAgent
from app.agents.repo_agent import RepoAgent
from app.agents.script_agent import ScriptAgent

class AgentManager:

    def __init__(self):
        self.agents = {
            "kubernetes": KubernetesAgent(),
            "cicd": CICDAgent(),
            "logs": LogAgent(),
            "repo": RepoAgent(),
            "script": ScriptAgent()
        }

    async def run_agents(self, user_input: str):
        results = []

        for name, agent in self.agents.items():
            if name in user_input.lower():
                result = await agent.run(user_input)
                results.append(result)

        return results
