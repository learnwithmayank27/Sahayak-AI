from app.agents.base_agent import BaseAgent

class KubernetesAgent(BaseAgent):
    name = "kubernetes-agent"

    async def run(self, input_data: str):
        return {
            "agent": self.name,
            "analysis": f"Kubernetes issue detected in: {input_data}",
            "solution": "Check pods: kubectl get pods -A"
        }
